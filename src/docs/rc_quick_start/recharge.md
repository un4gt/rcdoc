---
title: 充值与套餐
icon: fluent-mdl2:money
order: 2
footer: false
---

## 如何进行充值？

在 Right Code 里，主要有两种使用方式：

- `余额充值`：走按量付费，调用模型时会从余额里扣费
- `Codex 包月套餐`：按套餐额度使用，只给 Codex 用

:::warning 提醒
仅 `Codex` 有包月套餐；使用其他模型需要充值后按量付费。模型费用请看 [模型列表](/docs/rc_quick_start/models.html)。
:::

1. 进入后台页面，点击左侧面板的 `获取订阅` 一栏

2. 如图所示，最上方为额度充值，如果你想按量使用，直接充值余额即可，我们的充值倍率可查看下方「额度与套餐定价」部分

3. 如果你只想使用Codex，建议直接开套餐包

:::important 注意
**套餐包只能使用Codex，请不要买错！**
:::

![](/assets/image/rc_quick_start/rc-1.webp)

## 额度与套餐定价

<div class="pricing-notice">
  <iconify-icon icon="mdi:information-outline" width="20" height="20"></iconify-icon>
  <span>本站各模型 input_tokens、output_tokens、cached_tokens 等价格均和官网同步</span>
</div>

<div class="pricing-section">
  <h3 class="pricing-title">
    <iconify-icon icon="mdi:package-variant-closed" width="24" height="24"></iconify-icon>
    Codex 包月套餐
    <span class="pricing-subtitle">仅可用 Codex</span>
  </h3>
  <div class="pricing-extra">
    <p><strong>补充说明 1：</strong>多个 Codex 套餐可以叠加使用，例如同时开 2 个大包套餐，则每天可用额度是 <code>90 + 90 = 180$</code>。</p>
    <p><strong>补充说明 2：</strong>当全部 Codex 套餐额度用完后，默认会走余额按量扣费；是否会继续扣余额，取决于这个 <a href="/docs/rc_quick_start/apikey.html" style="text-decoration: underline;">ApiKey 权限配置</a>（是否允许使用余额）。</p>
  </div>
  <div class="pricing-cards">
    <div class="pricing-card">
      <div class="card-header small">
        <span class="card-name">小包套餐</span>
        <span class="card-badge">入门</span>
      </div>
      <div class="card-price">
        <span class="price-amount">45</span>
        <span class="price-unit">元</span>
      </div>
      <div class="card-features">
        <div class="feature-item">
          <iconify-icon icon="mdi:calendar-month" width="16" height="16"></iconify-icon>
          <span>有效期 30 天</span>
        </div>
        <div class="feature-item">
          <iconify-icon icon="mdi:cash-multiple" width="16" height="16"></iconify-icon>
          <span>每日 30$ + <span class="highlight-text">结转剩余</span></span>
        </div>
        <div class="feature-item">
          <iconify-icon icon="mdi:source-branch" width="16" height="16"></iconify-icon>
          <span>并发数 8</span>
        </div>
      </div>
    </div>
    <div class="pricing-card popular">
      <div class="card-header medium">
        <span class="card-name">中包套餐</span>
        <span class="card-badge">推荐</span>
      </div>
      <div class="card-price">
        <span class="price-amount">60</span>
        <span class="price-unit">元</span>
      </div>
      <div class="card-features">
        <div class="feature-item">
          <iconify-icon icon="mdi:calendar-month" width="16" height="16"></iconify-icon>
          <span>有效期 30 天</span>
        </div>
        <div class="feature-item">
          <iconify-icon icon="mdi:cash-multiple" width="16" height="16"></iconify-icon>
          <span>每日 60$ + <span class="highlight-text">结转剩余</span></span>
        </div>
        <div class="feature-item">
          <iconify-icon icon="mdi:source-branch" width="16" height="16"></iconify-icon>
          <span>并发数 12</span>
        </div>
      </div>
    </div>
    <div class="pricing-card">
      <div class="card-header large">
        <span class="card-name">大包套餐</span>
        <span class="card-badge">超值</span>
      </div>
      <div class="card-price">
        <span class="price-amount">75</span>
        <span class="price-unit">元</span>
      </div>
      <div class="card-features">
        <div class="feature-item">
          <iconify-icon icon="mdi:calendar-month" width="16" height="16"></iconify-icon>
          <span>有效期 30 天</span>
        </div>
        <div class="feature-item">
          <iconify-icon icon="mdi:cash-multiple" width="16" height="16"></iconify-icon>
          <span>每日 90$ + <span class="highlight-text">结转剩余</span></span>
        </div>
        <div class="feature-item">
          <iconify-icon icon="mdi:source-branch" width="16" height="16"></iconify-icon>
          <span>并发数 16</span>
        </div>
      </div>
    </div>
  </div>
  <div class="rollover-info">
    <div class="rollover-header">
      <iconify-icon icon="mdi:help-circle" width="24" height="24"></iconify-icon>
      <span>什么是结转剩余？</span>
      <span class="rollover-tag">重点规则</span>
    </div>
    <p class="rollover-summary">
      简单说：今天没用完的钱会带到明天；并且你每天拥有一次重置机会，系统会按“昨天剩余 + 今天新额度”来计算当天可用额度。
    </p>
    <div class="rollover-content">
      <div class="rollover-example">
        <div class="example-step">
          <span class="step-day">第1天</span>
          <span class="step-desc">套餐 90$，当天用掉 40$，还剩 50$</span>
        </div>
        <iconify-icon icon="mdi:arrow-right" width="20" height="20" class="step-arrow"></iconify-icon>
        <div class="example-step">
          <span class="step-day">第2天</span>
          <span class="step-desc">重置前 50$ + 重置后 90$ = <strong>140$</strong></span>
        </div>
        <iconify-icon icon="mdi:arrow-right" width="20" height="20" class="step-arrow"></iconify-icon>
        <div class="example-step">
          <span class="step-day">第3天</span>
          <span class="step-desc">继续按“前一天剩余 + 当天新额度”重新计算</span>
        </div>
      </div>
      <div class="rollover-notice">
        <iconify-icon icon="mdi:alert-circle" width="16" height="16"></iconify-icon>
        <span>注意：每天只有一次重置机会，且套餐购买第一天没有重置资格！如果当日未重置，会结转到第二天。</span>
      </div>
    </div>
  </div>
</div>

<div class="pricing-section">
  <h3 class="pricing-title">
    <iconify-icon icon="mdi:scale-balance" width="24" height="24"></iconify-icon>
    按量付费
    <span class="pricing-subtitle">Codex + Claude Code</span>
  </h3>
  <div class="payg-container">
    <div class="payg-rate">
      <span class="rate-label">充值比例</span>
      <span class="rate-value">0.2 元 = 站内 1$</span>
    </div>
    <div class="payg-cards">
      <div class="payg-card codex">
        <div class="payg-icon">
          <iconify-icon icon="hugeicons:chat-gpt" width="40" height="40"></iconify-icon>
        </div>
        <div class="payg-info">
          <span class="payg-name">Codex</span>
          <span class="payg-price">0.2 元/美金</span>
        </div>
      </div>
      <div class="payg-card claude">
        <div class="payg-icon">
          <iconify-icon icon="logos:claude-icon" width="36" height="36"></iconify-icon>
        </div>
        <div class="payg-info">
          <span class="payg-name">Claude Max 号池</span>
          <span class="payg-price">1 元/美金</span>
        </div>
      </div>
    </div>
  </div>
</div>

## 并发规则

<div class="rollover-info">
  <div class="rollover-header">
    <iconify-icon icon="mdi:source-branch" width="24" height="24"></iconify-icon>
    <span>并发说明</span>
    <span class="rollover-tag">重点规则</span>
  </div>
  <p class="rollover-summary">
    按这 5 条规则理解就不会乱：
  </p>
  <div class="rollover-content">
    <div class="rollover-example concurrency-rules">
      <div class="example-step">
        <span class="step-day">规则 1</span>
        <span class="step-desc">多个 Codex 套餐并发可以叠加，先得到你的「总套餐并发」。</span>
      </div>
      <div class="example-step">
        <span class="step-day">规则 2</span>
        <span class="step-desc">只要请求还在扣套餐余额，就按「总套餐并发」来限制。</span>
      </div>
      <div class="example-step">
        <span class="step-day">规则 3</span>
        <span class="step-desc">超过总套餐并发后，会尝试走余额按量扣费（前提：这个 Key 的 <a href="/docs/rc_quick_start/apikey.html" style="text-decoration: underline;">权限配置</a> 允许使用余额）。</span>
      </div>
      <div class="example-step">
        <span class="step-day">规则 4</span>
        <span class="step-desc">余额按量付费并发统一是 <strong>50</strong>（不分模型）。</span>
      </div>
      <div class="example-step">
        <span class="step-day">规则 5</span>
        <span class="step-desc">如果 Key 不允许使用余额，或者余额不足，会提示 <strong>429</strong>。</span>
      </div>
    </div>
  </div>
</div>

<style>
.pricing-notice {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 12px 16px;
  margin: 16px 0;
  background: linear-gradient(135deg, #e8f4fd 0%, #d6eaf8 100%);
  border-radius: 8px;
  border-left: 4px solid #3498db;
  color: #2980b9;
  font-size: 14px;
}

.pricing-section {
  margin: 24px 0;
}

.pricing-title {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 18px;
  font-weight: 600;
  color: #333;
  margin-bottom: 16px;
}

.pricing-subtitle {
  font-size: 13px;
  font-weight: 600;
  color: #b45309;
  margin-left: 6px;
  padding: 2px 8px;
  border-radius: 999px;
  background: linear-gradient(135deg, #fff4e5 0%, #ffe1bd 100%);
  border: 1px solid rgba(180, 83, 9, 0.2);
}

.pricing-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 16px;
}

.pricing-extra {
  margin-bottom: 14px;
  padding: 10px 14px;
  border-radius: 10px;
  background: linear-gradient(135deg, #fff7ed 0%, #ffedd5 100%);
  border-left: 4px solid #f97316;
}

.pricing-extra p {
  margin: 4px 0;
  font-size: 13px;
  line-height: 1.6;
  color: #9a3412;
}

.pricing-card {
  position: relative;
  padding: 20px;
  background: linear-gradient(135deg, #fff 0%, #f8f9fa 100%);
  border-radius: 12px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.06);
  border: 1px solid #eee;
  transition: all 0.3s ease;
}

.pricing-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
}

.pricing-card.popular {
  border: 2px solid #3498db;
  background: linear-gradient(135deg, #f0f9ff 0%, #e8f4fd 100%);
}

.card-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 12px;
}

.card-name {
  font-size: 16px;
  font-weight: 600;
  color: #333;
}

.card-badge {
  font-size: 11px;
  padding: 2px 8px;
  border-radius: 10px;
  background: #eee;
  color: #666;
}

.card-header.small .card-badge { background: #e8f5e9; color: #43a047; }
.card-header.medium .card-badge { background: #e3f2fd; color: #1976d2; }
.card-header.large .card-badge { background: #fff3e0; color: #f57c00; }

.card-price {
  display: flex;
  align-items: baseline;
  gap: 4px;
  margin-bottom: 16px;
}

.price-amount {
  font-size: 36px;
  font-weight: 700;
  color: #333;
}

.price-unit {
  font-size: 16px;
  color: #666;
}

.card-features {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.feature-item {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 13px;
  color: #666;
}

.highlight-text {
  display: inline-block;
  padding: 1px 6px;
  background: linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%);
  color: #e65100;
  border-radius: 4px;
  font-weight: 600;
  font-size: 12px;
}

.rollover-info {
  margin: 20px 0;
  background: rgba(255, 255, 255, 0.7);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-radius: 12px;
  border: 1px solid rgba(255, 255, 255, 0.8);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.06);
  overflow: hidden;
}

.rollover-header {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 8px;
  padding: 14px 20px;
  background: rgba(255, 255, 255, 0.5);
  border-bottom: 1px solid rgba(0, 0, 0, 0.06);
  color: #333;
  font-size: 16px;
  font-weight: 600;
}

.rollover-tag {
  margin-left: auto;
  padding: 4px 10px;
  border-radius: 999px;
  background: linear-gradient(135deg, #fff7ec 0%, #ffe2c4 100%);
  color: #b85b19;
  font-size: 12px;
  font-weight: 700;
  border: 1px solid rgba(224, 107, 49, 0.28);
}

.rollover-summary {
  margin: 0;
  padding: 14px 20px 0;
  color: #475569;
  font-size: 14px;
  line-height: 1.6;
  font-weight: 500;
}

.rollover-content {
  padding: 20px;
}

.rollover-example {
  display: flex;
  align-items: center;
  gap: 12px;
  flex-wrap: wrap;
  margin-bottom: 16px;
}

.concurrency-rules {
  display: grid;
  grid-template-columns: 1fr;
  gap: 10px;
}

.example-step {
  display: flex;
  flex-direction: column;
  gap: 4px;
  padding: 12px 16px;
  background: rgba(255, 255, 255, 0.8);
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
  border: 1px solid rgba(0, 0, 0, 0.04);
}

.step-day {
  font-size: 12px;
  color: #888;
  font-weight: 500;
}

.step-desc {
  font-size: 14px;
  color: #333;
  line-height: 1.6;
}

.step-arrow {
  color: #666;
  flex-shrink: 0;
}

.rollover-notice {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 10px 14px;
  background: rgba(231, 76, 60, 0.08);
  border-radius: 8px;
  border-left: 3px solid #e74c3c;
  color: #c0392b;
  font-size: 13px;
}

.payg-container {
  background: linear-gradient(135deg, #f8f9fa 0%, #eef1f5 100%);
  border-radius: 12px;
  padding: 20px;
}

.payg-rate {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 12px;
  padding: 12px;
  margin-bottom: 16px;
  background: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
}

.rate-label {
  font-size: 14px;
  color: #666;
}

.rate-value {
  font-size: 16px;
  font-weight: 600;
  color: #3498db;
}

.payg-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 12px;
}

.payg-card {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 16px;
  background: #fff;
  border-radius: 10px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
  transition: all 0.3s ease;
}

.payg-card:hover {
  transform: translateX(4px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
}

.payg-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 48px;
  height: 48px;
}

.payg-info {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.payg-name {
  font-size: 14px;
  font-weight: 600;
  color: #333;
}

.payg-price {
  font-size: 18px;
  font-weight: 700;
  color: #3498db;
}

[data-theme="dark"] .pricing-notice {
  background: linear-gradient(135deg, #1a3a4a 0%, #152d3a 100%);
  border-left-color: #3498db;
  color: #7ec8e3;
}

[data-theme="dark"] .pricing-title {
  color: #e8e8e8;
}

[data-theme="dark"] .pricing-subtitle {
  color: #ffc68a;
  background: rgba(180, 83, 9, 0.24);
  border-color: rgba(255, 198, 138, 0.24);
}

[data-theme="dark"] .pricing-card {
  background: linear-gradient(135deg, #2a2a2a 0%, #222 100%);
  border-color: #3a3a3a;
}

[data-theme="dark"] .pricing-card.popular {
  background: linear-gradient(135deg, #1a2d3a 0%, #152535 100%);
  border-color: #3498db;
}

[data-theme="dark"] .pricing-extra {
  background: rgba(249, 115, 22, 0.16);
  border-left-color: #fb923c;
}

[data-theme="dark"] .pricing-extra p {
  color: #fdba74;
}

[data-theme="dark"] .card-name {
  color: #e8e8e8;
}

[data-theme="dark"] .card-badge {
  background: #3a3a3a;
  color: #aaa;
}

[data-theme="dark"] .card-header.small .card-badge { background: #1b3d1f; color: #66bb6a; }
[data-theme="dark"] .card-header.medium .card-badge { background: #1a3a4a; color: #64b5f6; }
[data-theme="dark"] .card-header.large .card-badge { background: #3d2a1a; color: #ffb74d; }

[data-theme="dark"] .price-amount {
  color: #e8e8e8;
}

[data-theme="dark"] .price-unit {
  color: #aaa;
}

[data-theme="dark"] .feature-item {
  color: #aaa;
}

[data-theme="dark"] .highlight-text {
  background: linear-gradient(135deg, #4a3520 0%, #3d2a1a 100%);
  color: #ffb74d;
}

[data-theme="dark"] .rollover-info {
  background: rgba(45, 45, 45, 0.7);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-color: rgba(255, 255, 255, 0.1);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
}

[data-theme="dark"] .rollover-header {
  background: rgba(255, 255, 255, 0.05);
  border-bottom-color: rgba(255, 255, 255, 0.08);
  color: #e8e8e8;
}

[data-theme="dark"] .rollover-tag {
  background: rgba(224, 107, 49, 0.18);
  border-color: rgba(224, 107, 49, 0.35);
  color: #ffbd8a;
}

[data-theme="dark"] .rollover-summary {
  color: #c2c8d0;
}

[data-theme="dark"] .example-step {
  background: rgba(50, 50, 50, 0.8);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
  border-color: rgba(255, 255, 255, 0.05);
}

[data-theme="dark"] .step-arrow {
  color: #888;
}

[data-theme="dark"] .step-day {
  color: #888;
}

[data-theme="dark"] .step-desc {
  color: #e8e8e8;
}

[data-theme="dark"] .rollover-notice {
  background: rgba(231, 76, 60, 0.15);
  border-left-color: #e74c3c;
  color: #f1948a;
}

[data-theme="dark"] .payg-container {
  background: linear-gradient(135deg, #252525 0%, #1a1a1a 100%);
}

[data-theme="dark"] .payg-rate {
  background: #2a2a2a;
}

[data-theme="dark"] .rate-label {
  color: #aaa;
}

[data-theme="dark"] .payg-card {
  background: #2a2a2a;
}

[data-theme="dark"] .payg-name {
  color: #e8e8e8;
}
</style>
