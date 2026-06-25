I am sharing the dataset I created for Payments/cards variance analysis. Here is the detail about key attributes
1. Curr_rsn_cd : C - Closed card, R- Replaced, E - Expiry Change, B - Brand Flip
2. drc_code and de039_acq_resp_cd: Has 00 for approvals and 5,14,57, etc codes as decline reason codes
3. de048se22sf05_cit_mit_indctr: Has CIT/MIT indicator. This tells if it is customer initiated transaction (tap on mall) or merchant initiated (applepay)
4. de48_bank_merchant_advice_cd: Bank's merchant advice code, which tells bank what they should do for such type of transactions
5. cof_indicator: If its card-on-file or non-card-on-file

Story:
Why did declined transactions increase and approval rate drop in 2025 Q2 vs 2025 Q1?

<img width="812" height="207" alt="image" src="https://github.com/user-attachments/assets/4fbfab8e-5009-482e-8b33-1ac1d4dade6c" />

<img width="877" height="210" alt="image" src="https://github.com/user-attachments/assets/774edb50-7a5c-4548-b2fa-715ae17ba3c3" />
