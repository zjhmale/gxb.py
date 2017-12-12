#!/usr/bin/env python
# coding=utf-8

from gxb.api.block import BlockAPI
from functools import wraps

ba = BlockAPI()

def assert_resp(assertion):
  @wraps(assertion)
  def wrapper(*args, **kwargs):
    resp = None
    resp = assertion(*args, **kwargs)
    assert resp != None
  return wrapper

@assert_resp
def test_supply_api():
  return ba.get_supply()

@assert_resp
def test_block_info_api():
  return ba.get_block_info('5131961')

@assert_resp
def test_transaction_info_api():
  return ba.get_transaction_info('b9f36aacd871d7a4a6fb3f9adfe837a2bf6b0c79')

@assert_resp
def test_account_info_api():
  return ba.get_account_info('aaron')

@assert_resp
def test_account_balance_api():
  return ba.get_account_balance('aaron')

@assert_resp
def test_account_avatar_api():
  return ba.get_account_avatar('aaron')

@assert_resp
def test_product_info_api():
  return ba.get_product_info('1.17.3')
