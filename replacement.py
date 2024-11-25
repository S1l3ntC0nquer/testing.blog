import os
import re

# Dictionary with the words to be replaced and their replacements
replacements = {
    "陳子雋": "Kalpesh Solanki",
    "資安": "Cybersecurity",
    "駭客": "Hacker",
    "黑客": "Hacker",
    "程式設計": "Programming",
    "程式設計師": "Programmer",
    "程式設計博客": "Programming Blog",
    "程式設計部落格": "Programming Blog",
    "程式設計日誌": "Programming Diary",
    "筆記": "Notes",
    "網頁開發": "Web Development",
    "密碼學": "Cryptography",
    "簡": "Simplified Chinese",
    "繁": "Traditional Chinese",
    "博客": "Blog",
    "部落格": "Blog",
    "日誌": "Diary",
    "音樂": "Music",
    "隨便": "Random",
    "我的": "My",
    "關於": "About",
    "首頁": "Home",
    "訂閱": "Subscribe",
    "自我介紹": "Self Introduction",
    "資料": "Data",
    "留言板": "Message Board",
    "社交": "Social",
    "連結": "Link",
    "關閉": "Close",
    "分享": "Share",
    "最新": "Latest",
    "顯示": "Show",
    "提示": "Tips",
    "更多": "More",
    "技能": "Skills",
    "個人": "Personal",
    "作品": "Works",
    "作品集": "Portfolio",
    "簡介": "Introduction",
    "目標": "Goals",
    "夢想": "Dreams",
    "追求": "Pursuit",
    "人生": "Life",
    "讀書": "Books",
    "音樂": "Music",
    "運動": "Sports",
    "加載頭像":"Loading",
    "互動":"Engage",
    "興趣點":"Points of interest",
    "尋找你感興趣的領域":"Find your area of ​​interest",
    "文章":"Article",
    "顯示模式切換":"Theme",
    "邊欄顯示控制":"Panel",
    "熱評開關":"Popular",
    "音樂開關":"Play",
    "切換":"Switch",
    "通知":"Reminder",
    "你好呀":"Hello!",
    "陳子雋":"XploitOverlord",
    "程式設計部落格日誌":"hacker-blog",
    "程式設計部落格":"hacker-blog",
    "程式設計博客":"hacker-blog",
    "NCKU":"GTU",
    "Blake":"Kalpesh",
    "Chen": "Solanki",
    "CX330Blake": "S1l3ntC0nquer",
    "CX330": "S1l3ntC0nquer",
    "cx330":"S1l3ntC0nquer"
}

# Function to replace words in a file
def replace_in_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # Perform replacements only for the words in the dictionary
    for old_text, new_text in replacements.items():
        content = re.sub(rf"\b{re.escape(old_text)}\b", new_text, content)

    # Save the modified content back to the file
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)

# Function to walk through all files in a directory
def replace_in_directory(directory_path):
    for root, _, files in os.walk(directory_path):
        for file in files:
            # Process only .html files (you can add other file extensions as needed)
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                replace_in_file(file_path)
                print(f"Replaced content in: {file_path}")

# Main function
if __name__ == "__main__":
    # Specify the directory where the HTML files are located
    directory_path = input("Enter the directory path to process: ")

    replace_in_directory(directory_path)
    print("Replacement completed!")