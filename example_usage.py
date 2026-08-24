from client import PanEuropeanB2bWholesaleBrandsMarketplaceClient

def main():
    client = PanEuropeanB2bWholesaleBrandsMarketplaceClient()
    res = client.onboard_independent_retailer('Concept Store Berlin Mitte', 'Sustainable_Beauty_Wellness', 1200.0)
    print('Retailer ID: ' + res['retailer_account_id'] + ' | Shop: ' + res['shop_name'])
    print('Welcome Voucher: -EUR ' + str(res['welcome_voucher_discount_eur']) + ' | Net 60 Terms: ' + str(res['net_60_days_working_capital_credit_approved']))
    print('Free Pan-EU Shipping: ' + str(res['free_pan_european_shipping_unlocked']) + ' (Min Order: EUR ' + str(res['minimum_order_quantity_per_brand_eur']) + ')')

if __name__ == '__main__':
    main()
