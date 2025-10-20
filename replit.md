# SAMSAT SMART INFOBOARD - Kebumen Edition

## Overview
SAMSAT SMART INFOBOARD - Kebumen Edition is a Flask-based web application providing the public with essential information regarding SAMSAT Kebumen services. It aims to streamline access to information on vehicle registration (STNK) and tax, operating hours, required documents, and estimated costs through a professional, user-friendly interface with QR code integration. This project serves as a foundational component for a larger vision: a comprehensive, interactive official website for Satlantas Polres Kebumen.

## User Preferences
- Bahasa Indonesia untuk semua konten dan komentar
- Styling profesional untuk kantor pemerintahan
- Emoji untuk visual appeal
- Responsive dan mobile-friendly

## System Architecture
The application is built with Flask, employing a multi-page architecture to deliver dynamic content rendered from Markdown files. It features 8 main menus: Home, 5-Year Tax, Duplicate STNK, Inter-regional Transfer, BBN 1 & 2, Legal Basis, Gallery, and IKM (Community Satisfaction Index). The UI/UX is designed professionally with a blue gradient header, responsive navigation, and print-friendly styling. Legal documents are presented via embedded PDF viewers, and a gallery showcases SAMSAT activities. A fully integrated IKM survey system allows users to rate services with a star system and comments, displaying results on a real-time dashboard based on 9 criteria and categorized according to Permenpan RB No. 14/2017. Security features include CSRF protection, rate limiting (IKM: 50 per day, Feedback: 20 per hour), comprehensive security headers, input validation, and secure session management, aligning with OWASP Top 10 and BSSN standards.

## Recent Changes (October 2025)
- **BBN II Fee Update**: Removed BPNKB 10% charge from BBN II (second-hand vehicle transfer) per new 2025 regulation - now only PKB + OPSEN + admin fees, resulting in massive savings (motor: Rp 1-2M, mobil: Rp 10-20M)
- **IKM Rate Limit Adjustment**: Increased from 10 per hour to 50 per day to accommodate public survey participation from shared networks
- **Mutasi Processing Time**: Updated from 1-2 days to 4-5 working days based on real operational data
- **Favicon Added**: Professional logo-samsat.png as website favicon

## External Dependencies
- **Backend Framework**: Flask (Python 3.11)
- **Database**: PostgreSQL (Neon) for IKM survey data
- **Templating Engine**: Jinja2
- **Markdown Parser**: python-markdown
- **QR Code Generation**: qrcode + Pillow
- **Frontend Interactivity**: Vanilla JavaScript
- **Security**: Flask-WTF (CSRF protection), Flask-Limiter (rate limiting)