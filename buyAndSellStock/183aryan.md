#Buy and Sell Stocks - All version

##Buy and Sell Stocks - i
- You are given an array prices where prices[i] is the price of a given stock on the ith day.You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

- Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
- Constraints:
- ![image](https://user-images.githubusercontent.com/76700307/193417768-3ce04811-0343-416d-9bdc-7f7507300ff2.png)
- Example 1:
- ![image](https://user-images.githubusercontent.com/76700307/193417677-661ff76f-b63b-4107-85ec-e2ab283e4159.png)
- Example 2:
- ![image](https://user-images.githubusercontent.com/76700307/193417697-27fb77ef-cd48-4a17-9809-382fde396424.png)

- Code for this question in C++
- ![image](https://user-images.githubusercontent.com/76700307/193417739-521ce603-936a-4a58-9edb-2f82f114ca4a.png)

##Buy and Sell Stocks - ii
- You are given an integer array prices where prices[i] is the price of a given stock on the ith day.On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

- Find and return the maximum profit you can achieve.
- Constraints:
- ![image](https://user-images.githubusercontent.com/76700307/193417872-431068a3-793d-4de6-a246-90d86f12d6c5.png)
- Example 1:
- ![image](https://user-images.githubusercontent.com/76700307/193417885-0a32d80e-53bf-440e-b621-fd0a32f8869c.png)
- Example 2:
- ![image](https://user-images.githubusercontent.com/76700307/193417895-479909ed-42b2-454a-a4de-50925b762090.png)

- Code for this question in C++ using memoization :
- ![image](https://user-images.githubusercontent.com/76700307/193418032-794eadca-5176-414b-9ccd-acaf8e57ae4c.png)

##Buy and Sell Stocks - iii
- You are given an array prices where prices[i] is the price of a given stock on the ith day.Find the maximum profit you can achieve. You may complete at most two transactions.

- Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
- Constraints :
- ![image](https://user-images.githubusercontent.com/76700307/193418142-9383d676-9f40-400c-9361-13dbaa4a7bc9.png)
- Example 1:
- ![image](https://user-images.githubusercontent.com/76700307/193418166-9cd55a20-0457-4580-a2ad-2e5464d4740a.png)
- Example 2:
- ![image](https://user-images.githubusercontent.com/76700307/193418180-7f12ce6e-4b1a-4e58-b492-51cb7d6dde21.png)

- Code for this question in C++ using memoization :
- ![image](https://user-images.githubusercontent.com/76700307/193418215-228db53a-3f9a-4fe9-bff1-523a90ff4044.png)

##Buy and Sell Stocks - iv
- You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.Find the maximum profit you can achieve. You may complete at most k transactions.

- Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
- Constraints :
- ![image](https://user-images.githubusercontent.com/76700307/193418254-51320d13-d845-4fdb-927f-0963f3c2c4e9.png)
- Example 1:
- ![image](https://user-images.githubusercontent.com/76700307/193418310-77c0e0c1-04e3-410e-8fbf-9444e4dd6e99.png)
- Example 2:
- ![image](https://user-images.githubusercontent.com/76700307/193418322-1780d62a-25dd-4c2c-8b1d-226e6ad79eab.png)

- Code for this question in C++ using memoization and tabulation:
- ![image](https://user-images.githubusercontent.com/76700307/193418351-ce78151c-e441-41e1-bbe0-b7992c2e221f.png)

##Buy and Sell Stocks - with transaction fee
- You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.

- Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
- Constraints :
- ![image](https://user-images.githubusercontent.com/76700307/193418439-1af85184-3094-4845-88a7-c289a3cce477.png)
- Example 1:
- ![image](https://user-images.githubusercontent.com/76700307/193418458-cf67c885-5d35-419c-b84e-63d7dbb0fce4.png)
- Example 2:
- ![image](https://user-images.githubusercontent.com/76700307/193418469-d738342b-7af9-41a3-b7f4-56e25668c936.png)

- Code for this question in C++ using tabulation :
- ![image](https://user-images.githubusercontent.com/76700307/193418493-02fc9970-a3b6-4308-8232-fbf3a80861cb.png)

##Buy and Sell Stocks - with CoolDown
- You are given an array prices where prices[i] is the price of a given stock on the ith day. Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

- After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
- Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
- Constraints :
- ![image](https://user-images.githubusercontent.com/76700307/193418594-bd8ea881-0f40-46eb-8301-1b499d717efd.png)
- Example 1:
- ![image](https://user-images.githubusercontent.com/76700307/193418605-d7074567-15c4-4df2-a09b-cb137f0996e7.png)
- Example 2 :
- ![image](https://user-images.githubusercontent.com/76700307/193418620-d1156bcb-fbb2-466d-9095-63c4c3285106.png)

- Code for this question in C++ using memoization and tabulation :
- ![image](https://user-images.githubusercontent.com/76700307/193418650-f98cb41a-5f93-4b9c-911a-73470275d19c.png)

- That's all from my side. Thanks for reading.
