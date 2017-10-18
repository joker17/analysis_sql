create or replace view vo4_bondpayment as
select
	d.market_no market_no,
	c.inter_code inter_code,
	nvl(b.vc_report_code, ' ') report_code,
	a.l_pay_date installment_pay_date,
	nvl(a.en_pay_ratio, 0) installment_pay_rate,
	nvl(a.en_pay_amount, 0) installment_pay_balance,
	a.l_end_date expire_pay_date
from tbondpayratio a, tstockinfo  b, jc_tconvertintercode c, jc_tconvertmarketno d
where a.vc_inter_code = b.vc_inter_code(+)
and b.c_market_no = d.market_no_src
and d.market_no = c.market_no
and b.vc_report_code = c.report_code;