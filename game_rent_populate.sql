-- Populate Admin Table
INSERT INTO admin (admin_name, email, password) VALUES
('Kusk', 'kusk24@gmail.com', 'letmein1'),
('Sky', 'sky@gmail.com', 'letmein2'),
('Tommy', 'tommy@gmail.com', 'letmein3');

-- Populate Staff Table
INSERT INTO staff (staff_name, email, password, phone_number, salary, street_address, city, state, zip_code, type, admin_id, last_action) VALUES
('Alice', 'alice@gmail.com', 'staffpass1', '123-456-7890', 5000.00, '123 Main St', 'Anytown', 'CA', '90210', 'Full_Time', 1, 'Added'),
('Bob', 'bob@gmail.com', 'staffpass2', '987-654-3210', 3500.00, '456 Oak Ave', 'Springfield', 'IL', '62704', 'Part_Time', 2, 'Updated'),
('Charlie', 'charlie@gmail.com', 'staffpass3', '555-123-4567', 2000.00, '789 Pine Ln', 'Riverside', 'NY', '10001', 'Internship', 1, 'Updated'),
('David', 'david@gmail.com', 'staffpass4', '321-654-0987', 4500.00, '741 Cedar St', 'Los Angeles', 'CA', '90001', 'Full_Time', 3, 'Added'),
('Eve', 'eve@gmail.com', 'staffpass5', '741-852-9630', 3000.00, '852 Willow Rd', 'Houston', 'TX', '77002', 'Part_Time', 2, 'Updated'),
('Frank', 'frank@gmail.com', 'staffpass6', '369-258-1470', 2800.00, '963 Birch St', 'Phoenix', 'AZ', '85001', 'Internship', 3, 'Added'),
('Grace', 'grace@gmail.com', 'staffpass7', '258-369-1470', 5000.00, '753 Elm St', 'Seattle', 'WA', '98101', 'Full_Time', 1, 'Added');

-- Populate Customer Table
INSERT INTO customer (customer_name, email, password, phone_number, street_address, city, state, zip_code, staff_id, created_date) VALUES
('Kang Chul', 'kchul@gmail.com', 'customerpass1', '111-222-3333', '100 Elm Rd', 'Hill Valley', 'CA', '95000', 1, '2025-10-24'),
('Beverly', 'beverly@gmail.com', 'customerpass2', '444-555-6666', '200 Maple Dr', 'Gotham', 'NY', '10002', 2, '2025-10-25'),
('Soe', 'spp@gmail.com', 'customerpass3', '000-000-001', '300 Oak Rd', 'Star City', 'FL', '42069', 3, '2025-10-25'),
('Gracie', 'grace.davis@gmail.com', 'customerpass4', '777-888-9999', '400 Birch Ct', 'Metropolis', 'IL', '62705', 4, '2025-10-26'),
('Henry', 'henry@gmail.com', 'customerpass5', '666-777-8888', '500 Pine Ave', 'Central City', 'TX', '75001', 5, '2025-10-26'),
('Isabel', 'isabel@gmail.com', 'customerpass6', '555-444-3333', '600 Aspen Ln', 'Smallville', 'NV', '89101', 6, '2025-10-27'),
('Jack', 'jack@gmail.com', 'customerpass7', '222-333-4444', '700 Spruce St', 'Hawkins', 'IN', '46001', 7, '2025-10-28');

-- Populate Banned_Members Table
INSERT INTO banned_members (customer_id, reason, ban_date) VALUES
(3, 'Violation of terms of service', '2025-11-01'),
(5, 'Excessive late returns', '2025-11-02'),
(7, 'Damaged multiple game discs', '2025-11-03');

-- Populate Notice Table
INSERT INTO notice (reason, date, admin_id) VALUES
('New game rental policy', '2025-10-27', 1),
('Holiday hours', '2025-10-28', 2),
('System maintenance', '2025-11-05', 3),
('Upcoming game releases', '2025-11-10', 1),
('Discount on select rentals', '2025-11-15', 1),
('Membership benefits updated', '2025-11-20', 2),
('New payment methods available', '2025-11-25', 3);

INSERT INTO Game (game_name, release_date, platform, genre, rating, stock_number, price, image_link, admin_id, last_action) VALUES
('Black Myth: Wukong', '2024-08-20', 'PC', 'Action RPG', 'M', 10, 65, 'https://storage-asset.msi.com/event/2024/CND/black-myth-wukong/images/kv-m.jpg', 3, 'Added'),
('God of War Ragnarok', '2022-11-09', 'PS5', 'Action', 'M', 8, 50, 'https://i0.wp.com/www.consolecreatures.com/wp-content/uploads/2022/11/reviewgodofwar.webp', 1, 'Added'),
('The Legend of Zelda: Tears of the Kingdom', '2023-05-12', 'Nintendo Switch', 'Adventure', 'E10+', 15, 60, 'https://sitthinunt.com/wp-content/uploads/2023/05/zelda-breath-of-the-wild-1024x571.png', 2, 'Added'),
('Cyberpunk 2077', '2020-12-10', 'PC', 'RPG', 'M', 12, 35, 'https://cdn.prod.website-files.com/637d26e2dd50470752116a93/643c34803882725ac2e190b7_EGS_Cyberpunk2077_CDPROJEKTRED_S1_03_2560x1440-359e77d3cd0a40aebf3bbc130d14c5c7.jpg', 1, 'Updated'),
('Starfield', '2023-09-06', 'Xbox Series X', 'RPG', 'M', 10, 70, 'https://gaming-cdn.com/images/products/17580/orig/starfield-shattered-space-pc-game-steam-cover.jpg?v=1727440628', 3, 'Added'),
('Red Dead Redemption 2', '2018-10-26', 'PS4', 'Action', 'M', 7, 40, 'https://cdn1.epicgames.com/b30b6d1b4dfd4dcc93b5490be5e094e5/offer/RDR2476298253_Epic_Games_Wishlist_RDR2_2560x1440_V01-2560x1440-2a9ebe1f7ee202102555be202d5632ec.jpg', 2, 'Added'),
('Super Mario Bros. Wonder', '2023-10-20', 'Nintendo Switch', 'Platformer', 'E', 14, 55, 'https://i0.wp.com/mynintendonews.com/wp-content/uploads/2023/10/super_mario_bros_wonder_logo.jpeg?fit=1200%2C675&ssl=1', 1, 'Added'),
('The Witcher 3: Wild Hunt', '2015-05-19', 'PC', 'RPG', 'M', 10, 30, 'https://i.ytimg.com/vi/mMKZQLRkyfU/maxresdefault.jpg', 3, 'Updated'),
('Horizon Forbidden West', '2022-02-18', 'PS5', 'Action', 'T', 9, 50, 'https://i.ytimg.com/vi/wQATS4HOxdo/maxresdefault.jpg', 2, 'Added'),
('Call of Duty: Modern Warfare III', '2023-11-10', 'PC', 'FPS', 'M', 20, 70, 'https://platform.theverge.com/wp-content/uploads/sites/2/chorus/uploads/chorus_asset/file/25524871/modern_warfare_3_graphic_price.jpg?quality=90&strip=all&crop=7.8125,0,84.375,100', 3, 'Added'),
('Spider-Man 2', '2023-10-20', 'PS5', 'Action', 'T', 11, 60, 'https://image.api.playstation.com/vulcan/ap/rnd/202306/1219/e66c4ae18c5d8e3986a24599b293162a6f5c9eba22968d2c.jpg', 1, 'Added'),
('Final Fantasy XVI', '2023-06-22', 'PS5', 'RPG', 'M', 6, 55, 'https://assets-prd.ignimgs.com/2021/08/05/final-fantasy-xvi-button-1628180674117.jpg', 2, 'Updated'),
('Diablo IV', '2023-06-06', 'PC', 'Action RPG', 'M', 5, 65, 'https://www.gamespace.com/wp-content/uploads/2023/04/Diablo-IV-Beta-Retrospective.jpg', 3, 'Added'),
('Baldur’s Gate 3', '2023-08-03', 'PC', 'RPG', 'M', 10, 60, 'https://image.api.playstation.com/vulcan/ap/rnd/202302/2321/3098481c9164bb5f33069b37e49fba1a572ea3b89971ee7b.jpg', 1, 'Added'),
('Assassin’s Creed Mirage', '2023-10-05', 'PS5', 'Action', 'M', 8, 50, 'https://images.macrumors.com/t/U3uqJWtH5pmWX1CZKjC4Yc3t-Ew=/1600x/article-new/2024/04/Assassins-Creed-Mirage.jpg', 2, 'Updated'),
('Mortal Kombat 11', '2019-04-23', 'Xbox Series X', 'Fighting', 'M', 12, 60, 'https://assets.nintendo.com/image/upload/c_fill,w_1200/q_auto:best/f_auto/dpr_2.0/ncom/software/switch/70010000015154/3d45a55169bcdeccb5fc315d6c0fe7d8f2733a8545e744f1d28b3d68a69083d3', 3, 'Added'),
('Forza Horizon 5', '2021-11-09', 'PC', 'Racing', 'E', 10, 45, 'https://assets-prd.ignimgs.com/2021/12/21/forza-cropped-1640108250914.jpg', 1, 'Added'),
('Gears of War 6', '2025-09-15', 'Xbox Series X', 'TPS', 'M', 7, 70, 'https://roargamer.com/wp-content/uploads/2024/05/maxresdefault-13-min.jpg', 2, 'Added'),
('Resident Evil 4 Remake', '2023-03-24', 'PS5', 'Horror', 'M', 9, 60, 'https://i.ytimg.com/vi/j5Xv2lM9wes/maxresdefault.jpg', 3, 'Updated'),
('Metroid Prime 4', '2025-12-20', 'Nintendo Switch', 'Action', 'T', 6, 65, 'https://assets.nintendo.com/image/upload/ar_16:9,c_lpad,w_1240/b_white/f_auto/q_auto/ncom/software/switch/70010000084766/8e16460a2fc3be78fb99a411be9d51e4a8ca0d33d965da0c5b0f0ed291454e62', 1, 'Added'),
('Elden Ring: Shadow of the Erdtree', '2025-06-15', 'PC', 'Action RPG', 'M', 8, 60, 'https://pub-f354ec240bea480db7320bd0e29d972e.r2.dev/sites/2/2024/02/Elden-Ring-Hero-d2b3b43835cb49e5eb96.jpg', 2, 'Added');

-- Populate Rental Table
INSERT INTO rental (game_id, customer_id, status, rent_date, due_date) VALUES
(1, 1, 'Returned', '2025-10-10', '2025-10-17'),
(2, 2, 'Returned', '2025-10-11', '2025-10-18'),
(3, 3, 'Returned', '2025-10-12', '2025-10-19'),
(4, 4, 'Returned', '2025-10-13', '2025-10-20'),
(5, 5, 'Returned', '2025-10-14', '2025-10-21'),
(6, 6, 'Returned', '2025-10-15', '2025-10-22'),
(7, 7, 'Returned', '2025-10-16', '2025-10-23'),
(8, 1, 'Returned', '2025-10-17', '2025-10-24'),
(9, 2, 'Pending', '2025-10-18', '2025-10-25'),
(10, 3, 'Pending', '2025-10-19', '2025-10-26'),
(11, 4, 'Pending', '2025-10-20', '2025-10-27'),
(12, 5, 'Pending', '2025-10-21', '2025-10-28'),
(13, 6, 'Renting', '2025-10-22', '2025-10-29'),
(14, 7, 'Renting', '2025-10-23', '2025-10-30'),
(15, 1, 'Renting', '2025-10-24', '2025-10-31'),
(16, 2, 'Renting', '2025-10-25', '2025-11-01'); 

-- Populate Payment Table
INSERT INTO payment (rental_id, proof, method) VALUES
(1, 'http://example.com/payment1.jpg', 'Direct Bank'),
(2, 'http://example.com/payment2.jpg', 'PayPal'),
(3, 'http://example.com/payment3.jpg', 'PromptPay'),
(4, 'http://example.com/payment4.jpg', 'Direct Bank'),
(5, 'http://example.com/payment5.jpg', 'PayPal'),
(6, 'http://example.com/payment6.jpg', 'Direct Bank'),
(7, 'http://example.com/payment7.jpg', 'PromptPay'),
(8, 'http://example.com/payment8.jpg', 'Direct Bank'),
(9, 'http://example.com/payment9.jpg', 'PayPal'),
(10, 'http://example.com/payment10.jpg', 'PromptPay'),
(11, 'http://example.com/payment11.jpg', 'Direct Bank'),
(12, 'http://example.com/payment12.jpg', 'PayPal'),
(13, 'http://example.com/payment13.jpg', 'PromptPay'),
(14, 'http://example.com/payment14.jpg', 'Direct Bank'),
(15, 'http://example.com/payment15.jpg', 'PayPal'),
(16, 'http://example.com/payment16.jpg', 'PromptPay');

-- Populate Game_Reports Table
INSERT INTO game_reports (rental_id, reason, report_date, detail, attachment) VALUES
(1, 'Game disc scratched', '2025-10-25', 'Game disc has visible scratches and skips during gameplay.', 'http://example.com/report1.jpg'),
(2, 'Case damaged', '2025-10-26', 'Game case is broken.', 'http://example.com/report2.jpg'),
(3, 'Missing manual', '2025-10-27', 'Instruction manual missing from the package.', 'http://example.com/report3.jpg'),
(4, 'Disc unreadable', '2025-10-28', 'Game does not load properly.', 'http://example.com/report4.jpg'),
(5, 'Wrong game received', '2025-10-29', 'Customer received a different game.', 'http://example.com/report5.jpg'),
(6, 'Severe scratches', '2025-10-30', 'Multiple deep scratches.', 'http://example.com/report6.jpg'),
(7, 'Box art damaged', '2025-10-31', 'Cover art severely torn.', 'http://example.com/report7.jpg');