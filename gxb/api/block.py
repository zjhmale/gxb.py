#!/usr/bin/env python
# coding=utf-8

import base64
import requests

class BlockAPI(object):
  API_URL = "http://block.gxb.io/api"

  def get_supply(self):
    return requests.get("%s/%s" % (self.API_URL, "supply")).json()

  def get_block_info(self, block_height):
    return requests.get("%s/%s/%s" % (self.API_URL, "block", block_height)).json()

  def get_transaction_info(self, tx_id):
    return requests.get("%s/%s/%s" % (self.API_URL, "transaction", tx_id)).json()

  def get_account_info(self, account_id_or_name):
    return requests.get("%s/%s/%s" % (self.API_URL, "account", account_id_or_name)).json()

  def get_account_balance(self, account_id_or_name):
    return requests.get("%s/%s/%s" % (self.API_URL, "account_balance", account_id_or_name)).json()

  def get_account_avatar(self, account_name):
    img = b''
    resp = requests.get("%s/%s/%s" % (self.API_URL, "header", account_name))
    for chunk in resp.iter_content(chunk_size=128):
      img += chunk

    return base64.b64encode(img)

  def get_product_info(self, product_id):
    return requests.get("%s/%s/%s" % (self.API_URL, "product", product_id)).json()
