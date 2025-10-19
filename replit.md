# SAMSAT SMART INFOBOARD - Kebumen Edition

## Overview
SAMSAT SMART INFOBOARD - Kebumen Edition is a Flask-based web application providing the public with essential information regarding SAMSAT Kebumen services. It aims to streamline access to information on vehicle registration (STNK) and tax, operating hours, required documents, and estimated costs through a professional, user-friendly interface with QR code integration. This project serves as a foundational component for a larger vision: a comprehensive, interactive official website for Satlantas Polres Kebumen.

## User Preferences
- Bahasa Indonesia untuk semua konten dan komentar
- Styling profesional untuk kantor pemerintahan
- Emoji untuk visual appeal
- Responsive dan mobile-friendly

## System Architecture
The application is built with Flask, employing a multi-page architecture to deliver dynamic content rendered from Markdown files. It features 8 main menus: Home, 5-Year Tax, Duplicate STNK, Inter-regional Transfer, BBN 1 & 2, Legal Basis, Gallery, and IKM (Community Satisfaction Index). The UI/UX is designed professionally with a blue gradient header, responsive navigation, and print-friendly styling. Legal documents are presented via embedded PDF viewers, and a gallery showcases SAMSAT activities. A fully integrated IKM survey system allows users to rate services with a star system and comments, displaying results on a real-time dashboard based on 9 criteria and categorized according to Permenpan RB No. 14/2017. Security features include CSRF protection, rate limiting, comprehensive security headers, input validation, and secure session management, aligning with OWASP Top 10 and BSSN standards.

## External Dependencies
- **Backend Framework**: Flask (Python 3.11)
- **Database**: PostgreSQL (Neon) for IKM survey data
- **Templating Engine**: Jinja2
- **Markdown Parser**: python-markdown
- **QR Code Generation**: qrcode + Pillow
- **Frontend Interactivity**: Vanilla JavaScript
- **Security**: Flask-WTF (CSRF protection), Flask-Limiter (rate limiting)