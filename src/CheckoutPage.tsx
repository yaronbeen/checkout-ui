import React from 'react';
import {TextProps, ButtonProps} from '@shopify/checkout-ui-extensions';
import {Heading, Text, Button, BlockStack, Layout} from './components';

const CheckoutPage = () => {
  return (
    <Layout className="checkout-page">
      <BlockStack gap="400">
        <Heading level={1}>Checkout</Heading>
        <Text size="base">
          Please review your order and proceed to payment.
        </Text>
        <Button kind="primary" onPress={() => alert('Checkout initiated!')}>
          Proceed to Payment
        </Button>
      </BlockStack>
    </Layout>
  );
};

export default CheckoutPage;