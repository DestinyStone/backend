# Frontend Code Style Guide
This document outlines coding standards based on the Vue.js Official Style Guide and established JavaScript conventions.

## 1. General Standards
### 1.1. Application Scope
* Applies to all frontend development (JavaScript, HTML, and Vue components)

### 1.2. Naming Conventions
* Avoid non-descriptive names (examples: a_2, temp_var)
* Implement proper naming formats (examples: loginState, isFilling)

## 2. Naming Protocols
* Component Files: Apply camelCase formatting (examples: contact.vue, userProfile.vue)
* Component Tags: Implement kebab-case formatting (examples: <el-button>, <user-profile>)
* Function Names: Utilize camelCase formatting (examples: loadContacts, validateForm)
* Variable Names: Apply camelCase formatting (examples: loading, formRef)
* Constant Values: Use UPPERCASE_WITH_UNDERSCORES (examples: API_BASE_URL, MAX_RETRY_COUNT)
* Component Properties: Implement kebab-case formatting (examples: :user-data="userInfo", @click="submitForm")

## 3. Code Formatting
### 3.1. Basic Formatting
* Indentation: Implement 2-space indentation (avoid tab characters)
* Statement Termination: Include semicolons at statement conclusions
### 3.2. Import Organization
* Maintain separate import lines with grouping in this sequence:
* Framework imports (examples: vue, vue-router)
* External library imports (examples: element-plus, axios)
* Internal module imports (examples: from '../api', from './components/...')

## 4. Component Architecture
* Script Setup: Implement syntax for new components
* Style Scoping: Apply scoped attribute to component styles to prevent CSS leakage
### 4.1. Component Implementation
* Apply ref for basic data types and individual object/array references
* Implement reactive for complex data structures requiring direct modification
* Define functions using const functionName = () => {} syntax
### 4.2. Lifecycle Management
* Directly integrate lifecycle hooks (onMounted, onUpdated) within

# 5. Application Architecture & API Integration
### 5.1. Core Principles
* API Management: Centralize API interactions through dedicated modules (examples: api.js, api/index.js)
* Asynchronous Operations: Employ async/await patterns for handling asynchronous tasks
* Error Management: Enclose API calls within try...catch blocks and implement user notification systems
### 5.2. State Management
* Implement loading state tracking (example: loading = ref(false)) for API operations
* Utilize loading states to deactivate interactive elements and prevent duplicate requests