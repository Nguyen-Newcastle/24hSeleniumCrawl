Giới thiệu
Dự án này được thiết kế để thu thập dữ liệu từ trang web 24h.com.vn bằng cách sử dụng Selenium. Dự án được container hóa với Docker và được điều phối bằng Docker Compose. Dự án bao gồm các script để trích xuất các bài viết mới nhất từ các mục khác nhau của trang web và lấy metadata cho các bài viết nổi bật.

Cấu trúc dự án
Copy code
SeleniumCrawl/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── scripts/
│   ├── extract_latest_articles_on_sections.py
│   ├── read_article_metadata.py
│   ├── read_highlighted_articles.py
│   ├── read_menu_titles.py
│   └── utils/
│       └── selenium_setup.py

Yêu cầu
Docker
Docker Compose

Hướng dẫn thiết lập

1. Clone Repository
bash
Copy code
git clone https://github.com/Nguyen-Newcastle/24hSeleniumCrawl.git
cd SeleniumCrawl

2. Build và Chạy các Docker Containers
Đảm bảo rằng Docker và Docker Compose đã được cài đặt trên máy của bạn. Sau đó, thực hiện lệnh sau:

bash
Copy code
docker-compose up --build
Lệnh này sẽ thực hiện các hành động sau:

Build Docker image cho dự án.
Thiết lập Selenium Hub.
Thiết lập một Selenium Node với Chrome.
Chạy các script để trích xuất và hiển thị dữ liệu bài viết.

3. Các thành phần của dự án
Dockerfile
Dockerfile thiết lập môi trường để chạy các script Python. Nó sử dụng một image Python gọn nhẹ, cài đặt các gói cần thiết từ requirements.txt, và thiết lập lệnh mặc định.

docker-compose.yml
Tệp này điều phối các dịch vụ khác nhau:

selenium-hub: Hub trung tâm cho Selenium Grid.
selenium-node-chrome1: Một node Chrome kết nối với hub.
latest-articles-on-sections: Dịch vụ chạy script để trích xuất các bài viết mới nhất từ các mục khác nhau của trang web 24h.com.vn.
highlighted-articles: Dịch vụ chạy script để đọc các bài viết nổi bật được hiển thị trên trang chính của trang web 24h.com.vn.

4. Mô tả các script

extract_latest_articles_on_sections.py
Script này thu thập các bài viết mới nhất từ các mục khác nhau của trang web 24h.com.vn.

read_article_metadata.py
Script này trích xuất metadata từ các bài viết, bao gồm mô tả, URL chuẩn, hình ảnh Open Graph, ngày xuất bản và nội dung bài viết.

read_highlighted_articles.py
Script này lấy metadata cho các bài viết nổi bật được hiển thị trên trang chính của trang web 24h.com.vn.

read_menu_titles.py
Script này đọc các tiêu đề menu và URL của chúng từ trang web 24h.com.vn.

utils/selenium_setup.py
Các hàm tiện ích để thiết lập và kết thúc WebDriver của Selenium.

5. Chạy dự án
Để chạy dự án và xem kết quả của các script, sử dụng lệnh sau:

bash
Copy code
docker-compose up
Các log sẽ được hiển thị trên console, cho thấy tiến trình và kết quả của các script.

Ghi chú bổ sung
Đảm bảo rằng bạn có kết nối internet ổn định vì các script phụ thuộc vào việc thu thập dữ liệu trực tuyến.
Điều chỉnh GRID_MAX_SESSION và SE_NODE_MAX_SESSIONS trong docker-compose.yml dựa trên nhu cầu và khả năng hệ thống của bạn.
Khắc phục sự cố
Nếu WebDriver của Selenium không kết nối được, kiểm tra log của Docker để tìm lỗi và đảm bảo rằng Selenium Hub và Nodes đã được cấu hình và chạy đúng cách.
Đảm bảo rằng tất cả các cổng cần thiết (4444 và 5555) đều khả dụng và không bị firewall chặn.
Đóng góp
Vui lòng mở các issue hoặc gửi pull request để cải tiến và sửa lỗi.

README này cung cấp một cái nhìn tổng quan và hướng dẫn từng bước để thiết lập và chạy dự án SeleniumCrawl để thu thập dữ liệu web bằng cách sử dụng Selenium, Docker và Docker Compose.
