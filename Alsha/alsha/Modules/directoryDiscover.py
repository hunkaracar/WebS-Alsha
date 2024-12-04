import requests
import time
import sys
from colorama import init, Fore, Back, Style

def discover_directory(base_url):

    directories = [
        "/index.html",
        "/admin",
        "/administrator",
        "/login",
        "/signup",
        "/profile",
        "/search",
        "/contact",
        "/about",
        "/home",
        "/products",
        "/blog",
        "/gallery",
        "/news",
        "/help",
        "/faq",
        "/terms",
        "/privacy",
        "/cart",
        "/checkout",
        "/category",
        "/events",
        "/services",
        "/support",
        "/download",
        "/uploads",
        "/media",
        "/sitemap",
        "/rss",
        "/subscribe",
        "/unsubscribe",
        "/forum",
        "/feedback",
        "/newsletter",
        "/subscribe.html",
        "/unsubscribe.html",
        "/terms-of-service",
        "/privacy-policy",
        "/register",
        "/activate",
        "/verify",
        "/forgot-password",
        "/reset-password",
        "/dashboard",
        "/settings",
        "/notifications",
        "/messages",
        "/inbox",
        "/outbox",
        "/notifications",
        "/admin-panel",
        "/blog-post",
        "/user",
        "/users",
        "/public",
        "/private",
        "/search-results",
        "/404",
        "/403",
        "/500",
        "/maintenance",
        "/coming-soon",
        "/pricing",
        "/testimonials",
        "/career",
        "/jobs",
        "/resources",
        "/events-calendar",
        "/sitemap.xml",
        "/robots.txt",
        "/feed",
        "/archive",
        "/gallery",
        "/photos",
        "/videos",
        "/press",
        "/partners",
        "/donate",
        "/api",
        "/docs",
        "/features",
        "/plugins",
        "/themes",
        "/fonts",
        "/css",
        "/js",
        "/images",
        "/assets",
        "/static",
        "/uploads",
        "/download",
        "/media",
        "/cdn",
        "/ajax",
        "/xhr",
        "/tmp",
        "/logs",
        "/backup",
        "/wp-admin",
        "/wp-content",
        "/wp-includes",
        "/admin.php",
        "/wp-config.php",
        "/administrator.php",
        "/wp-content/uploads",
        "/wp-content/plugins",
        "/adminpanel/login.php",
        "/adminpanel/plugins",
        "/backup-db",
        "/backup-files",
        "/inc/includes",
        "/inc/assets",
        "/inc/config.php",
        "/inc/plugins",
        "/adminpanel.php",
        "/login.php",
        "/wp-login.php",
        "/adminpanel",
        "/inc",
        "/default.aspx",
        "/login.aspx",
        "/register.aspx",
        "/profile.aspx",
        "/admin.aspx",
        "/dashboard.aspx",
        "/search.aspx",
        "/products.aspx",
        "/cart.aspx",
        "/checkout.aspx",
        "/news.aspx",
        "/gallery.aspx",
        "/blog.aspx",
        "/yonetim/Giris.aspx",
        "/contact.aspx",
        "/about.aspx",
        "/services.aspx",
        "/faq.aspx",
        "/privacy.aspx",
        "/terms.aspx",
        "/sitemap.aspx"
    ]

    print("Discovery Url.....")
    print(f"Target Site -> {base_url}")
    print("-----------------------------------------------------------------------\n")
    time.sleep(3)

    try:
        for directory in directories:
            url = base_url + directory
            response = requests.get(url,verify=True)

            if response.status_code == 200:
                print(Fore.GREEN + f"[+]Discovery {directory} in {base_url}\n" + Fore.RESET)
                time.sleep(2)

            elif response.status_code == 400:
                print(f"Return Bad Requests 400 and {directory} in not {base_url}\n")
                time.sleep(2)

            elif response.status_code == 403:
                print(f"Return Forbidden 403 and {directory} in not {base_url}\n")
                time.sleep(2)

            elif response.status_code == 404:
                print(f"Return Not Found 404 and {directory} in not {base_url}\n")
                time.sleep(2)

            elif response.status_code == 500:
                print(f"Return Internal Server Error 500 and {directory} in not {base_url}\n")
                time.sleep(2)

            else:
                return False

    except KeyboardInterrupt:
        print(Fore.RED + "\nProgram Terminated:::" + Fore.RESET)
        sys.exit(0)

    except Exception as e:
        print(f"Error => {e}")
