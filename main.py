from requests.adapters import HTTPAdapter, Retry
from tqdm import tqdm
import os
import requests
import string
import openpyxl
from pyfiglet import Figlet
from colorama import init, Fore
import sys
import time
from colorama import init, Fore
from tabulate import tabulate
from colorama import init, Fore
import subprocess
from pytube import YouTube
import re

def get_colored_input(prompt, color):
    return input(color + prompt + Fore.RESET)

def index():
    init()
    f = Figlet(font='slant')
    print(Fore.GREEN,"welcome to")
    print(Fore.YELLOW,"Dawnloader V version 0.1")
    ascii_art = f.renderText('Dawnloader V')
    table_data = [
        [Fore.GREEN + "create by:", "bagus wirayuda" + Fore.RESET]
    ]
    table = tabulate(table_data, tablefmt="grid")
    print(Fore.BLUE + ascii_art + Fore.RESET)
    horizontal_line = Fore.RED + "============================================================" + Fore.RESET
    print(table)
    print(horizontal_line)
    print(Fore.YELLOW,"silahkan pilih menu yg anda ingin gunakan")
    print("+-------------------------------+")
    print("| No. |      Pilihan            |")
    print("+-------------------------------+")
    print("|  1  | youtube video dawnload  |")
    print("|  2  | youtube audio dawnload  |")
    print("|  3  | Tiktok downloader       |")
    print("|  4  | Facebook Downloader     |")
    print("|  5  | Instagram Downloader    |")
    print("|  5  | Twitter Downloader      |")
    print("|  0  |      Keluar             |")
    print("+-------------------------------+")
    
def get_user_choice():
    while True:
        user_input = input("Masukkan pilihan Anda (1/2/3/0): ")
        if user_input in ['1', '2', '3', '4','0']:
            return user_input
        else:
            print("Pilihan tidak valid. Silakan masukkan nomor pilihan yang benar.")
    
def download_youtube_video(url, output_path=None):
    try:
        yt = YouTube(url)
        video_stream = yt.streams.get_highest_resolution()
        video_title = yt.title
        file_size = video_stream.filesize
        print(Fore.GREEN, "Judul video:", video_title)
        print(Fore.GREEN, "Ukuran Video: {:.2f} MB".format(file_size / (1024 * 1024)))
        print(Fore.CYAN, "Sedang mendownload. Sabar ya...")
        if output_path:
            video_stream.download(output_path)
        else:
            video_stream.download()
        print(Fore.CYAN, "Download selesai.")
    except Exception as e:
        print(Fore.RED, "Gagal di-download. Periksa link dan jaringan cuy:", str(e))
   
def download_audio_as_mp3(video_url):
    try:
        yt = YouTube(video_url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        audio_stream.download(filename_prefix="audio_")
        print("Unduhan audio berhasil")
    except Exception as e:
        print("Gagal mengunduh audio:", str(e))
        
def tiktok_dawnload():
    api_url = f"https://api.akuari.my.id/downloader/tiktok?link={link}"
    response = requests.get(api_url)
    data = response.json()
    video_url = data.get("respon", {}).get("media")
    description = data.get('respon', {}).get("description")
    if video_url and description:
        filtered_description = re.sub(r'[^a-zA-Z0-9\s]', '', description)
        filtered_description = re.sub(r'\s+', ' ', filtered_description).strip()
        video_response = requests.get(video_url)
        video_filename = f"{filtered_description}.mp4"
        with open(video_filename, "wb") as video_file:
            video_file.write(video_response.content)
        print(f"Video berhasil diunduh dan disimpan sebagai {video_filename}")
    else:
        print("Video tanpa watermark tidak ditemukan.")

def facebook_dawnload():
    api_url = f"https://api.akuari.my.id/downloader/fbdl2?link={link}"
    waktu = str(int(time.time()))
    response = requests.get(api_url)
    data = response.json()
    video_url = data.get("hasil", [])[0].get("url", "")
    if video_url:
        video_response = requests.get(video_url)
        with open(f"facebook video {waktu}.mp4", "wb") as video_file:
            video_file.write(video_response.content)
        print(f"Video berhasil diunduh dan disimpan sebagai facebook video{waktu}.mp4")
    else:
        print("sepertinya video bersifat private")


if __name__ == "__main__":
    while True:
        index() 
        user_choice = get_user_choice() 
        link = get_colored_input("Masukkan linknya cuy: ", Fore.GREEN)

        if user_choice == '1':
            print("Anda memilih Video Download.")
            video_url = link
            output_directory = None
            download_youtube_video(video_url, output_directory)
        elif user_choice == '2':
            print("Anda memilih Audio Download (MP3).")
            download_audio_as_mp3(link)
        elif user_choice == '3':
            print("tiktok dawnload video")
            tiktok_dawnload() 
            break
        elif user_choice == '4':
            print("facebook video dawnload")
            facebook_dawnload()
            break
        continue_choice = input("Lakukan tindakan lain? (ya/tidak): ")
        if continue_choice.lower() != 'ya':
            break

    
        
        
