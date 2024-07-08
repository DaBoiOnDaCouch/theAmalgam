from time import sleep
import argparse
import pytube


def download_audio(video_url, output_path):
	try:
		yt = pytube.YouTube(video_url)
		audio_stream = yt.streams.filter(only_audio=True).first()

		filename = 'downloaded_audio.mp3'
		audio_stream.download(output_path=output_path, filename=filename)

		print(f"Audio downloaded to {output_path}/{filename}")
		print("Success!")
		sleep(2.5)

		main()

	# Really good error handling
	except pytube.exceptions.RegexMatchError:
		print("The URL didn't work, dummy. Try providing a valid link.")
		sleep(2.5)

		main()



def main():
	parser = argparse.ArgumentParser(description="Enter YouTube link of a video to download its audio (will auto-convert to MP3).")
	parser.add_argument("--output", default="./", help="Output folder path (default: current directory)")

	args = parser.parse_args()

	# Grab user input
	video_url = input("Insert a YouTube URL to download the audio from: ")

	# Download the audio
	download_audio(video_url, args.output)


if __name__ == "__main__":
	main()
