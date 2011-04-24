from zope.component import adapter
from collective.cart.core.interfaces import ICart as ICoreCart
from collective.cart.core.interfaces import (
    IUpdateCart,
)
from collective.cart.shipping.interfaces import (
    ICart,
    IPortal,
    IShippingMethod,
)

@adapter(IUpdateCart)
def set_shipping_cost(event):
    cart = event.cart
    method = IPortal(cart).selected_shipping_method
    weight = ICart(cart).weight
    price = float(ICoreCart(cart).subtotal)
    cost = IShippingMethod(method).shipping_cost(weight, price)
    item = dict(shipping_cost = cost)
    cart.totals.update(item)

