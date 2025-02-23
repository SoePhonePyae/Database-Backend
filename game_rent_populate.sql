-- Populate Admin Table
INSERT INTO admin (admin_name, email, password) VALUES
('Kusk', 'kusk24@gmail.com', 'letmein1'),
('Sky', 'sky@gmail.com', 'letmein2'),
('Tommy', 'tommy@gmail.com', 'letmein3');

-- Populate Staff Table
INSERT INTO staff (staff_name, email, password, phone_number, salary, street_address, city, state, zip_code, type, admin_id, last_action) VALUES
('Alice', 'alice@gmail.com', 'staffpass1', '123-456-7890', 5000.00, '123 Main St', 'Anytown', 'CA', '90210', 'Full_Time', 1, NOW()),
('Bob', 'bob@gmail.com', 'staffpass2', '987-654-3210', 3500.00, '456 Oak Ave', 'Springfield', 'IL', '62704', 'Part_Time', 2, NOW()),
('Charlie', 'charlie@gmail.com', 'staffpass3', '555-123-4567', 2000.00, '789 Pine Ln', 'Riverside', 'NY', '10001', 'Internship', 1, NOW());

-- Populate Customer Table
INSERT INTO customer (customer_name, email, password, phone_number, street_address, city, state, zip_code, staff_id, created_date) VALUES
('Kang Chul', 'kchul@gmail.com', 'customerpass1', '111-222-3333', '100 Elm Rd', 'Hill Valley', 'CA', '95000', 1, '2025-10-24'),
('Beverly', 'beverly@gmail.com', 'customerpass2', '444-555-6666', '200 Maple Dr', 'Gotham', 'NY', '10002', 2, '2025-10-25'),
('Soe', 'spp@gmail.com', 'customerpass3', '000-000-001', '300 Oak Rd', 'Star City', 'FL', '42069', 2, '2025-10-25'),
('Gracie', 'grace.davis@gmail.com', 'customerpass4', '777-888-9999', '400 Birch Ct', 'Metropolis', 'IL', '62705', 3, '2025-10-26');

-- Populate Banned_Members Table
INSERT INTO banned_members (customer_id, reason, ban_date) VALUES
(3, 'Violation of terms of service', '2025-11-01');

-- Populate Notice Table
INSERT INTO notice (reason, date, admin_id) VALUES
('New game rental policy', '2025-10-27', 1),
('Holiday hours', '2025-10-28', 2);

-- Populate Game Table
INSERT INTO game (game_name, release_date, platform, genre, rating, stock_number, image_link, admin_id, last_action) VALUES
('Elden Ring', '2022-02-25', 'PC', 'Action', 'M', 10, 'http://example.com/gameA.jpg', 1, NOW()),
('Halo Infinite', '2021-12-08', 'Xbox Series X', 'FPS', 'T', 5, 'http://example.com/gameB.jpg', 2, NOW()),
('Civilization VII', '2025-02-11', 'PC', 'Strategy', 'E', 10, 'http://example.com/gameC.jpg', 1, NOW());

-- Populate Rental Table
INSERT INTO rental (game_id, customer_id, status, rent_date, due_date, duration) VALUES
(1, 1, 'Renting', '2025-10-20', '2025-10-27', 7),
(2, 2, 'Returned', '2025-10-15', '2025-10-22', 7),
(3, 4, 'Pending', '2025-10-25', '2025-11-01', 7);

-- Populate Payment Table
INSERT INTO payment (rental_id, proof, method) VALUES
(1, 'http://example.com/payment1.jpg', 'Credit Card'),
(2, 'http://example.com/payment2.jpg', 'PayPal');

-- Populate Game_Reports Table
INSERT INTO game_reports (rental_id, reason, report_date, detail, attachment) VALUES
(1, 'Game disc scratched', '2025-10-25', 'Game disc has visible scratches and skips during gameplay.', 'http://example.com/report1.jpg');