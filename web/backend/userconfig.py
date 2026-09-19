import bcrypt
import random
import smtplib
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv
from email.message import EmailMessage
from database import conectar