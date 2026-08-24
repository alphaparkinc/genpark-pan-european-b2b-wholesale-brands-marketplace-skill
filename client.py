class PanEuropeanB2bWholesaleBrandsMarketplaceClient:
    def onboard_independent_retailer(self, shop_name='Boutique Le Marais Paris', primary_category='Artisan_Home_Decor', first_order_subtotal_eur=850.0):
        return {
            'retailer_account_id': 'ank_ret_8812',
            'shop_name': shop_name,
            'category': primary_category,
            'welcome_voucher_discount_eur': 100.0,
            'net_60_days_working_capital_credit_approved': True,
            'free_pan_european_shipping_unlocked': True,
            'minimum_order_quantity_per_brand_eur': 100.0
        }
