def addBagPayload(pid, qty):
    body = {
        "deviceType": "WEBSITE",
        "domain": "nykaa",
        "appVersion": "2.8.1",
        "store": "nykaa",
        "pro": "false",
        "items": [
            {
                "productId": pid,
                "quantity": qty
            }
        ],
        "customer_group_id": "11"
    }
    return body
