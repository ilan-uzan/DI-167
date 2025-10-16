'use strict';

// API Configuration
const API_KEY = 'f937766d99342468de826d93';
const BASE_URL = 'https://v6.exchangerate-api.com/v6';

// DOM Elements
const elements = {
  amount: document.getElementById('amount'),
  fromCurrency: document.getElementById('fromCurrency'),
  toCurrency: document.getElementById('toCurrency'),
  fromSymbol: document.getElementById('fromSymbol'),
  switchBtn: document.getElementById('switchBtn'),
  convertBtn: document.getElementById('convertBtn'),
  resultSection: document.getElementById('resultSection'),
  originalAmount: document.getElementById('originalAmount'),
  originalCurrency: document.getElementById('originalCurrency'),
  convertedAmount: document.getElementById('convertedAmount'),
  convertedCurrency: document.getElementById('convertedCurrency'),
  rateInfo: document.getElementById('rateInfo'),
  loading: document.getElementById('loading'),
  loadingText: document.getElementById('loadingText'),
  error: document.getElementById('error'),
  errorMsg: document.getElementById('errorMsg')
};

// State
let currencies = {};
let isLoading = false;

// Initialize app
document.addEventListener('DOMContentLoaded', function() {
  loadCurrencies();
  setupEventListeners();
});

// Setup event listeners
function setupEventListeners() {
  elements.convertBtn.addEventListener('click', convertCurrency);
  elements.switchBtn.addEventListener('click', switchCurrencies);
  elements.amount.addEventListener('input', handleAmountChange);
  elements.fromCurrency.addEventListener('change', handleCurrencyChange);
  elements.toCurrency.addEventListener('change', handleCurrencyChange);
}

// Load supported currencies
async function loadCurrencies() {
  showLoading('Loading currencies...');
  
  try {
    const response = await fetch(`${BASE_URL}/${API_KEY}/codes`);
    
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`);
    }
    
    const data = await response.json();
    
    if (data.result === 'success') {
      currencies = {};
      data.supported_codes.forEach(([code, name]) => {
        currencies[code] = name;
      });
      
      populateCurrencySelectors();
      hideLoading();
    } else {
      throw new Error(data['error-type'] || 'Failed to load currencies');
    }
  } catch (error) {
    console.error('Error loading currencies:', error);
    showError(`Failed to load currencies: ${error.message}`);
  }
}

// Populate currency selectors
function populateCurrencySelectors() {
  const options = Object.entries(currencies)
    .map(([code, name]) => `<option value="${code}">${code} - ${name}</option>`)
    .join('');
  
  elements.fromCurrency.innerHTML = `<option value="">Select currency</option>${options}`;
  elements.toCurrency.innerHTML = `<option value="">Select currency</option>${options}`;
  
  // Set default currencies
  elements.fromCurrency.value = 'USD';
  elements.toCurrency.value = 'EUR';
  updateCurrencySymbol();
}

// Convert currency
async function convertCurrency() {
  const amount = parseFloat(elements.amount.value);
  const fromCurrency = elements.fromCurrency.value;
  const toCurrency = elements.toCurrency.value;
  
  // Validation
  if (!amount || amount <= 0) {
    showError('Please enter a valid amount');
    return;
  }
  
  if (!fromCurrency || !toCurrency) {
    showError('Please select both currencies');
    return;
  }
  
  if (fromCurrency === toCurrency) {
    showError('Please select different currencies');
    return;
  }
  
  if (isLoading) return;
  
  showLoading('Converting currency...');
  
  try {
    const response = await fetch(`${BASE_URL}/${API_KEY}/pair/${fromCurrency}/${toCurrency}/${amount}`);
    
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`);
    }
    
    const data = await response.json();
    
    if (data.result === 'success') {
      displayResult(data, amount, fromCurrency, toCurrency);
      hideLoading();
    } else {
      throw new Error(data['error-type'] || 'Conversion failed');
    }
  } catch (error) {
    console.error('Error converting currency:', error);
    showError(`Conversion failed: ${error.message}`);
  }
}

// Display conversion result
function displayResult(data, amount, fromCurrency, toCurrency) {
  const convertedAmount = data.conversion_result;
  const rate = data.conversion_rate;
  
  elements.originalAmount.textContent = amount.toLocaleString('en-US', {
    minimumFractionDigits: 2,
    maximumFractionDigits: 2
  });
  elements.originalCurrency.textContent = fromCurrency;
  
  elements.convertedAmount.textContent = convertedAmount.toLocaleString('en-US', {
    minimumFractionDigits: 2,
    maximumFractionDigits: 2
  });
  elements.convertedCurrency.textContent = toCurrency;
  
  elements.rateInfo.textContent = `1 ${fromCurrency} = ${rate.toFixed(4)} ${toCurrency}`;
  
  elements.resultSection.style.display = 'block';
}

// Switch currencies
function switchCurrencies() {
  const fromValue = elements.fromCurrency.value;
  const toValue = elements.toCurrency.value;
  const amount = elements.amount.value;
  
  // Swap currencies
  elements.fromCurrency.value = toValue;
  elements.toCurrency.value = fromValue;
  
  // Update symbol
  updateCurrencySymbol();
  
  // Hide result section
  elements.resultSection.style.display = 'none';
  
  // Clear amount
  elements.amount.value = '';
}

// Handle amount input change
function handleAmountChange() {
  // Hide result when amount changes
  elements.resultSection.style.display = 'none';
}

// Handle currency change
function handleCurrencyChange() {
  // Hide result when currency changes
  elements.resultSection.style.display = 'none';
  updateCurrencySymbol();
}

// Update currency symbol
function updateCurrencySymbol() {
  const fromCurrency = elements.fromCurrency.value;
  
  if (fromCurrency) {
    // Get currency symbol (simplified mapping)
    const symbols = {
      'USD': '$', 'EUR': '€', 'GBP': '£', 'JPY': '¥', 'CAD': 'C$',
      'AUD': 'A$', 'CHF': 'CHF', 'CNY': '¥', 'SEK': 'kr', 'NZD': 'NZ$',
      'MXN': '$', 'SGD': 'S$', 'HKD': 'HK$', 'NOK': 'kr', 'TRY': '₺',
      'RUB': '₽', 'INR': '₹', 'BRL': 'R$', 'ZAR': 'R', 'KRW': '₩'
    };
    
    elements.fromSymbol.textContent = symbols[fromCurrency] || fromCurrency;
  } else {
    elements.fromSymbol.textContent = '$';
  }
}

// Show loading state
function showLoading(message = 'Loading...') {
  isLoading = true;
  elements.loadingText.textContent = message;
  elements.loading.classList.remove('hidden');
  elements.error.classList.add('hidden');
  elements.convertBtn.disabled = true;
}

// Hide loading state
function hideLoading() {
  isLoading = false;
  elements.loading.classList.add('hidden');
  elements.convertBtn.disabled = false;
}

// Show error message
function showError(message) {
  elements.errorMsg.textContent = message;
  elements.error.classList.remove('hidden');
  elements.loading.classList.add('hidden');
  elements.convertBtn.disabled = false;
}