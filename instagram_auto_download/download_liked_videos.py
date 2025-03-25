import json
import yt_dlp

# Load the JSON file - use raw string for path to avoid escape sequence issues
with open(r"E:\mausam\Downloads\Python\scripting\likes.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Extract video links from liked posts
video_links = []
for post in data["likes_media_likes"]:  # Access the correct JSON structure
    # Extract href from string_list_data
    if post.get("string_list_data"):
        href = post["string_list_data"][0].get("href")
        if href:
            video_links.append(href)

# Remove duplicates
# Remove None values and duplicates
video_links = list(set(filter(None, video_links)))

# Check if there are videos to download
if not video_links:
    print("No videos found in your liked posts.")
else:
    # Configure yt-dlp options
    ydl_opts = {
        'format': 'best',  # Download best quality
        'outtmpl': '%(title)s.%(ext)s',  # Output template
    }

    # Download each video
    print(f"Found {len(video_links)} videos to download.")
    for i, video_url in enumerate(video_links, 1):
        print(f"\nDownloading video {i}/{len(video_links)}")
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_url])
        except Exception as e:
            print(f"Error downloading {video_url}: {str(e)}")

    print("\nDownload complete!")
