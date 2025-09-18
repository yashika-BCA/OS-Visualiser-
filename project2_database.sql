CREATE DATABASE os_timeline;
USE os_timeline;

CREATE TABLE operating_systems (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    year VARCHAR(255),
    developer VARCHAR(255),
    company VARCHAR(255),
    about TEXT
);

drop table operating_systems;

INSERT INTO operating_systems (name, year, developer, company, about) VALUES
('GM-NAA I/O', '1956', 'General Motors & NAA', 'IBM', 'First batch OS for IBM 704; automated job execution'),
('SHARE OS', '1959', 'SHARE User Group', 'IBM', 'Enabled program sharing and better I/O'),
('IBSYS', '1960', 'IBM', 'IBM', 'Batch OS with job control for IBM 7090'),
('FMS', '1960s', 'IBM', 'IBM', 'Fortran Monitor System; optimized for Fortran programs'),
('CTSS', '1961', 'MIT', 'IBM', 'First time-sharing OS; allowed multiple users'),
('Multics', '1965–69', 'MIT, Bell Labs, GE', 'GE, later Honeywell', 'Introduced segmentation, dynamic linking, and security'),
('UNIX', '1971', 'Ken Thompson, Dennis Ritchie', 'Bell Labs (AT&T)', 'Portable, multitasking OS; foundation for many modern OSes'),
('CP/M', '1974', 'Gary Kildall', 'Digital Research', 'Early OS for microcomputers; inspired MS-DOS'),
('MS-DOS', '1981', 'Microsoft (based on QDOS)', 'Microsoft', 'Command-line OS for IBM PCs; dominated the 1980s'),
('Mac OS (System 1)', '1984', 'Apple', 'Apple', 'First commercial GUI OS; introduced icons and windows'),
('Windows 1.0', '1985', 'Microsoft', 'Microsoft', 'GUI shell over MS-DOS; start of Windows series'),
('AmigaOS', '1985', 'Commodore', 'Commodore', 'Multitasking GUI OS for Amiga computers'),
('OS/2', '1987', 'IBM & Microsoft', 'IBM', 'GUI-based multitasking OS; later split from Microsoft'),
('Windows 3.0', '1990', 'Microsoft', 'Microsoft', 'First successful Windows GUI; introduced Program Manager'),
('Linux', '1991', 'Linus Torvalds', 'Open-source community', 'UNIX-like OS; widely used in servers, desktops, and Android'),
('Windows 95', '1995', 'Microsoft', 'Microsoft', 'Integrated MS-DOS and Windows; introduced Start menu'),
('BeOS', '1995', 'Be Inc.', 'Be Inc.', 'Multimedia-focused OS with symmetric multiprocessing'),
('macOS X (now macOS)', '2001', 'Apple', 'Apple', 'UNIX-based; introduced Aqua interface and Terminal'),
('Windows XP', '2001', 'Microsoft', 'Microsoft', 'Stable, user-friendly; widely adopted'),
('Android', '2008', 'Google', 'Google', 'Linux-based mobile OS; most used smartphone OS'),
('iOS', '2007', 'Apple', 'Apple', 'Mobile OS for iPhone; known for security and smooth UX'),
('Chrome OS', '2009', 'Google', 'Google', 'Lightweight OS for Chromebooks; browser-based'),
('Windows 7', '2009', 'Microsoft', 'Microsoft', 'Fast, stable, and widely loved desktop OS'),
('Tizen', '2012', 'Linux Foundation, Samsung', 'Samsung', 'OS for smart TVs, wearables, and IoT'),
('Windows 8', '2012', 'Microsoft', 'Microsoft', 'Introduced Metro UI; optimized for touchscreens'),
('Ubuntu Touch', '2013', 'Canonical', 'Canonical', 'Mobile version of Ubuntu; open-source'),
('Windows 10', '2015', 'Microsoft', 'Microsoft', 'Unified platform; introduced Cortana and virtual desktops'),
('KaiOS', '2017', 'KaiOS Technologies', 'KaiOS Technologies', 'Lightweight OS for feature phones with smart capabilities'),
('HarmonyOS', '2019', 'Huawei', 'Huawei', 'Cross-device OS; microkernel-based; for phones, TVs, IoT'),
('Fuchsia OS', '2021', 'Google', 'Google', 'Microkernel-based (Zircon); modular and scalable'),
('Windows 11', '2021', 'Microsoft', 'Microsoft', 'Modern UI, Snap Layouts, Android app support'),
('macOS Monterey', '2021', 'Apple', 'Apple', 'Introduced Universal Control and Shortcuts'),
('Android 12', '2021', 'Google', 'Google', 'Material You design; privacy dashboard'),
('iOS 15', '2021', 'Apple', 'Apple', 'Focus Mode, Live Text, FaceTime upgrades'),
('Ubuntu 22.04 LTS', '2022', 'Canonical', 'Canonical', 'Long-term support Linux distro; GNOME-based'),
('macOS Ventura', '2022', 'Apple', 'Apple', 'Introduced Stage Manager and Continuity Camera'),
('Android 13', '2022', 'Google', 'Google', 'Improved privacy and multilingual support'),
('Windows Server 2022', '2022', 'Microsoft', 'Microsoft', 'Enterprise OS with hybrid cloud and security enhancements'),
('macOS Sequoia', '2024', 'Apple', 'Apple', 'Latest macOS with AI features and ecosystem enhancements'),
('Android 15', '2025', 'Google', 'Google', 'Latest Android version with AI personalization and privacy tools'),
('macOS Tahoe 26', '2025', 'Apple', 'Apple', 'Final Intel-supported macOS; unveiled at WWDC 2025');

SELECT * FROM os_timeline.operating_systems;



