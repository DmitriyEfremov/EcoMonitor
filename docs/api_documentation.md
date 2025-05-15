
### Create




| Method | URL |
|--------|-----|
| POST | /status/create |

#### Parameters
| Name | In | Description | Required |
|------|----|-------------|----------|

##### Request Body
| Field | Type | Description | Required |
|-------|------|-------------|----------|
| name | string |  | Required |

##### Response (200)
| Field | Type | Description |
|-------|------|-------------|
| name | string |  |
| id | integer |  |

##### Response (422)
| Field | Type | Description |
|-------|------|-------------|
| detail | array |  |

---

### Read




| Method | URL |
|--------|-----|
| GET | /status/ |

#### Parameters
| Name | In | Description | Required |
|------|----|-------------|----------|

##### Response (200)
| Field | Type | Description |
|-------|------|-------------|

---

### Read




| Method | URL |
|--------|-----|
| GET | /status/{status_id} |

#### Parameters
| Name | In | Description | Required |
|------|----|-------------|----------|
| status_id | path |  | Required |

##### Response (200)
| Field | Type | Description |
|-------|------|-------------|
| name | string |  |
| id | integer |  |

##### Response (422)
| Field | Type | Description |
|-------|------|-------------|
| detail | array |  |

---

### Update




| Method | URL |
|--------|-----|
| PUT | /status/update-info |

#### Parameters
| Name | In | Description | Required |
|------|----|-------------|----------|

##### Request Body
| Field | Type | Description | Required |
|-------|------|-------------|----------|
| name | string |  | Required |
| id | integer |  | Required |

##### Response (200)
| Field | Type | Description |
|-------|------|-------------|
| name | string |  |
| id | integer |  |

##### Response (422)
| Field | Type | Description |
|-------|------|-------------|
| detail | array |  |

---

### Delete




| Method | URL |
|--------|-----|
| DELETE | /status/delete/{status_id} |

#### Parameters
| Name | In | Description | Required |
|------|----|-------------|----------|
| status_id | path |  | Required |

##### Response (204)
| Field | Type | Description |
|-------|------|-------------|

##### Response (422)
| Field | Type | Description |
|-------|------|-------------|
| detail | array |  |

---

### Create File




| Method | URL |
|--------|-----|
| POST | /file/create |

#### Parameters
| Name | In | Description | Required |
|------|----|-------------|----------|

##### Request Body
| Field | Type | Description | Required |
|-------|------|-------------|----------|
| user_id | string |  | Required |
| type_file | string |  | Required |
| eco_problem_id | integer |  | Required |
| storage_id | integer |  | Required |
| created_at | string |  | Required |

##### Response (200)
| Field | Type | Description |
|-------|------|-------------|
| user_id | string |  |
| type_file | string |  |
| eco_problem_id | integer |  |
| storage_id | integer |  |
| created_at | string |  |
| id | integer |  |

##### Response (422)
| Field | Type | Description |
|-------|------|-------------|
| detail | array |  |

---

### Read Files




| Method | URL |
|--------|-----|
| GET | /file/ |

#### Parameters
| Name | In | Description | Required |
|------|----|-------------|----------|

##### Response (200)
| Field | Type | Description |
|-------|------|-------------|

---

### Read File




| Method | URL |
|--------|-----|
| GET | /file/{file_id} |

#### Parameters
| Name | In | Description | Required |
|------|----|-------------|----------|
| file_id | path |  | Required |

##### Response (200)
| Field | Type | Description |
|-------|------|-------------|
| user_id | string |  |
| type_file | string |  |
| eco_problem_id | integer |  |
| storage_id | integer |  |
| created_at | string |  |
| id | integer |  |

##### Response (422)
| Field | Type | Description |
|-------|------|-------------|
| detail | array |  |

---

### Update File




| Method | URL |
|--------|-----|
| PUT | /file/update-info |

#### Parameters
| Name | In | Description | Required |
|------|----|-------------|----------|

##### Request Body
| Field | Type | Description | Required |
|-------|------|-------------|----------|
| user_id | string |  | Required |
| type_file | string |  | Required |
| eco_problem_id | integer |  | Required |
| storage_id | integer |  | Required |
| created_at | string |  | Required |

##### Response (200)
| Field | Type | Description |
|-------|------|-------------|
| user_id | string |  |
| type_file | string |  |
| eco_problem_id | integer |  |
| storage_id | integer |  |
| created_at | string |  |

##### Response (422)
| Field | Type | Description |
|-------|------|-------------|
| detail | array |  |

---

### Delete File




| Method | URL |
|--------|-----|
| DELETE | /file/delete/{file_id} |

#### Parameters
| Name | In | Description | Required |
|------|----|-------------|----------|
| file_id | path |  | Required |

##### Response (204)
| Field | Type | Description |
|-------|------|-------------|

##### Response (422)
| Field | Type | Description |
|-------|------|-------------|
| detail | array |  |

---

### Create Type Incident




| Method | URL |
|--------|-----|
| POST | /type_incident/create |

#### Parameters
| Name | In | Description | Required |
|------|----|-------------|----------|

##### Request Body
| Field | Type | Description | Required |
|-------|------|-------------|----------|
| name | string |  | Required |

##### Response (200)
| Field | Type | Description |
|-------|------|-------------|
| name | string |  |
| id | integer |  |

##### Response (422)
| Field | Type | Description |
|-------|------|-------------|
| detail | array |  |

---

### Read Type Incidents




| Method | URL |
|--------|-----|
| GET | /type_incident/ |

#### Parameters
| Name | In | Description | Required |
|------|----|-------------|----------|

##### Response (200)
| Field | Type | Description |
|-------|------|-------------|

---

### Read Type Incident




| Method | URL |
|--------|-----|
| GET | /type_incident/{type_incident_id} |

#### Parameters
| Name | In | Description | Required |
|------|----|-------------|----------|
| type_incident_id | path |  | Required |

##### Response (200)
| Field | Type | Description |
|-------|------|-------------|
| name | string |  |
| id | integer |  |

##### Response (422)
| Field | Type | Description |
|-------|------|-------------|
| detail | array |  |

---

### Update Type Incident




| Method | URL |
|--------|-----|
| PUT | /type_incident/update-info |

#### Parameters
| Name | In | Description | Required |
|------|----|-------------|----------|

##### Request Body
| Field | Type | Description | Required |
|-------|------|-------------|----------|
| name | string |  | Required |
| id | integer |  | Required |

##### Response (200)
| Field | Type | Description |
|-------|------|-------------|
| name | string |  |
| id | integer |  |

##### Response (422)
| Field | Type | Description |
|-------|------|-------------|
| detail | array |  |

---

### Delete Type Incident




| Method | URL |
|--------|-----|
| DELETE | /type_incident/delete/{type_incident_id} |

#### Parameters
| Name | In | Description | Required |
|------|----|-------------|----------|
| type_incident_id | path |  | Required |

##### Response (204)
| Field | Type | Description |
|-------|------|-------------|

##### Response (422)
| Field | Type | Description |
|-------|------|-------------|
| detail | array |  |

---

### Create Eco Problem




| Method | URL |
|--------|-----|
| POST | /eco_problem/create |

#### Parameters
| Name | In | Description | Required |
|------|----|-------------|----------|

##### Request Body
| Field | Type | Description | Required |
|-------|------|-------------|----------|
| creator_id | string |  | Required |
| manager_id | string |  | Required |
| title | string |  | Required |
| description | string |  | Required |
| status_id | integer |  | Required |
| type_incident_id | integer |  | Required |
| longitude | string |  | Required |
| latitude | string |  | Required |
| is_closed | boolean |  | Optional |

##### Response (200)
| Field | Type | Description |
|-------|------|-------------|
| creator_id | string |  |
| manager_id | string |  |
| title | string |  |
| description | string |  |
| status_id | integer |  |
| type_incident_id | integer |  |
| longitude | string |  |
| latitude | string |  |
| is_closed | boolean |  |
| id | integer |  |

##### Response (422)
| Field | Type | Description |
|-------|------|-------------|
| detail | array |  |

---

### Read Eco Problems




| Method | URL |
|--------|-----|
| GET | /eco_problem/ |

#### Parameters
| Name | In | Description | Required |
|------|----|-------------|----------|

##### Response (200)
| Field | Type | Description |
|-------|------|-------------|

---

### Read Eco Problem




| Method | URL |
|--------|-----|
| GET | /eco_problem/{eco_problem_id} |

#### Parameters
| Name | In | Description | Required |
|------|----|-------------|----------|
| eco_problem_id | path |  | Required |

##### Response (200)
| Field | Type | Description |
|-------|------|-------------|
| creator_id | string |  |
| manager_id | string |  |
| title | string |  |
| description | string |  |
| status_id | integer |  |
| type_incident_id | integer |  |
| longitude | string |  |
| latitude | string |  |
| is_closed | boolean |  |
| id | integer |  |

##### Response (422)
| Field | Type | Description |
|-------|------|-------------|
| detail | array |  |

---

### Update Eco Problem




| Method | URL |
|--------|-----|
| PUT | /eco_problem/update-info |

#### Parameters
| Name | In | Description | Required |
|------|----|-------------|----------|

##### Request Body
| Field | Type | Description | Required |
|-------|------|-------------|----------|
| creator_id | string |  | Required |
| manager_id | string |  | Required |
| title | string |  | Required |
| description | string |  | Required |
| status_id | integer |  | Required |
| type_incident_id | integer |  | Required |
| longitude | string |  | Required |
| latitude | string |  | Required |
| is_closed | boolean |  | Optional |
| id | integer |  | Required |

##### Response (200)
| Field | Type | Description |
|-------|------|-------------|
| creator_id | string |  |
| manager_id | string |  |
| title | string |  |
| description | string |  |
| status_id | integer |  |
| type_incident_id | integer |  |
| longitude | string |  |
| latitude | string |  |
| is_closed | boolean |  |
| id | integer |  |

##### Response (422)
| Field | Type | Description |
|-------|------|-------------|
| detail | array |  |

---

### Update Eco Problem Status




| Method | URL |
|--------|-----|
| PATCH | /eco_problem/update-status/{eco_problem_id} |

#### Parameters
| Name | In | Description | Required |
|------|----|-------------|----------|
| eco_problem_id | path |  | Required |
| status_id | query |  | Required |

##### Response (200)
| Field | Type | Description |
|-------|------|-------------|

##### Response (422)
| Field | Type | Description |
|-------|------|-------------|
| detail | array |  |

---

### Update Eco Problem Manager




| Method | URL |
|--------|-----|
| PATCH | /eco_problem/update-manager/{eco_problem_id} |

#### Parameters
| Name | In | Description | Required |
|------|----|-------------|----------|
| eco_problem_id | path |  | Required |
| manager_id | query |  | Required |

##### Response (200)
| Field | Type | Description |
|-------|------|-------------|

##### Response (422)
| Field | Type | Description |
|-------|------|-------------|
| detail | array |  |

---

### Close Eco Problem




| Method | URL |
|--------|-----|
| PUT | /eco_problem/close-eco-problem/{eco_problem_id} |

#### Parameters
| Name | In | Description | Required |
|------|----|-------------|----------|
| eco_problem_id | path |  | Required |

##### Response (200)
| Field | Type | Description |
|-------|------|-------------|

##### Response (422)
| Field | Type | Description |
|-------|------|-------------|
| detail | array |  |

---

### Delete Eco Problem




| Method | URL |
|--------|-----|
| DELETE | /eco_problem/delete/{eco_problem_id} |

#### Parameters
| Name | In | Description | Required |
|------|----|-------------|----------|
| eco_problem_id | path |  | Required |

##### Response (204)
| Field | Type | Description |
|-------|------|-------------|

##### Response (422)
| Field | Type | Description |
|-------|------|-------------|
| detail | array |  |

---
