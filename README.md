# Readme doc.help doctors parser v0.01a

A tiny app for parsing doctors from site, dicts with doctors exported from
[doc.help](https://doc.help/msk/doctor). Provide a single function as the default
export, `main`, which have pagination, and async methods.

## To Do 
For mass parsing you need add proxies to get requests, without it you would be
restricted from accessing the site.

## Usage

Setup requirements first, and after this run main.py 
```python
pip3 install -r requirements.txt
```

doctors.txt would output something along the lines of:

```json
{
  "ex_last_name": null,
  "hospitals": [
    {
      "schedule": [
        "0800-2100",
        "0800-2100",
        "0800-2100",
        "0800-2100",
        "0800-2100",
        "0900-1700",
        "0900-1700"
      ],
      "address": "107045, г.Москва, ул.Сретенский тупик, 4",
      "subways": [
        {
          "distance": 0.1,
          "line": {
            "color": "F07E24",
            "id": "5dc8ca26-029f-4e20-857b-4944c34a97c0",
            "title": "Калужско-Рижская"
          },
          "location": null,
          "id": "454b6949-4f54-4217-a1db-018b55a87ff1",
          "title": "Сухаревская",
          "slug": "suharevskaya"
        },
        {
          "distance": 0.6,
          "line": {
            "color": "BED12C",
            "id": "cfa7eabe-d284-478e-9e51-14f8e1bb9de3",
            "title": "Люблинско-Дмитровская"
          },
          "location": null,
          "id": "c5c16ccf-2112-4dc8-b654-508c9325531a",
          "title": "Сретенский бульвар",
          "slug": "sretenskij-bulvar"
        },
        {
          "distance": 0.7,
          "line": {
            "color": "F07E24",
            "id": "5dc8ca26-029f-4e20-857b-4944c34a97c0",
            "title": "Калужско-Рижская"
          },
          "location": null,
          "id": "c7ffe353-f047-4604-a5bd-5bdbe1e4e399",
          "title": "Тургеневская",
          "slug": "turgenevskaya"
        }
      ],
      "phone_suffix": 8535,
      "location": {
        "lon": 37.6335758,
        "lat": 55.7710635
      },
      "id": "d65da382-9c99-4f86-99a2-925d42c0d5e5",
      "title": "Медицинский центр Новая Поликлиника м. Сухаревская",
      "slug": "novaya-poliklinika-m-suharevskaya-d5e5",
      "timeslots": [
        {
          "busy": false,
          "slot": "2021-09-09T08:00:00"
        },
        {
          "busy": false,
          "slot": "2021-09-09T08:30:00"
        },
        {
          "busy": false,
          "slot": "2021-09-09T09:00:00"
        },
        {
          "busy": false,
          "slot": "2021-09-09T09:30:00"
        },
        {
          "busy": false,
          "slot": "2021-09-09T10:00:00"
        },
        {
          "busy": false,
          "slot": "2021-09-09T10:30:00"
        },
        {
          "busy": false,
          "slot": "2021-09-09T11:00:00"
        },
        {
          "busy": false,
          "slot": "2021-09-09T11:30:00"
        },
        {
          "busy": false,
          "slot": "2021-09-09T12:00:00"
        },
        {
          "busy": false,
          "slot": "2021-09-09T12:30:00"
        },
        {
          "busy": false,
          "slot": "2021-09-09T13:00:00"
        },
        {
          "busy": false,
          "slot": "2021-09-09T13:30:00"
        },
        {
          "busy": false,
          "slot": "2021-09-09T14:00:00"
        },
        {
          "busy": false,
          "slot": "2021-09-09T14:30:00"
        },
        {
          "busy": false,
          "slot": "2021-09-09T15:00:00"
        },
        {
          "busy": false,
          "slot": "2021-09-09T15:30:00"
        },
        {
          "busy": false,
          "slot": "2021-09-09T16:00:00"
        },
        {
          "busy": false,
          "slot": "2021-09-09T16:30:00"
        },
        {
          "busy": false,
          "slot": "2021-09-09T17:00:00"
        },
        {
          "busy": false,
          "slot": "2021-09-09T17:30:00"
        },
        {
          "busy": false,
          "slot": "2021-09-09T18:00:00"
        },
        {
          "busy": false,
          "slot": "2021-09-09T18:30:00"
        },
        {
          "busy": false,
          "slot": "2021-09-09T19:00:00"
        },
        {
          "busy": false,
          "slot": "2021-09-09T19:30:00"
        },
        {
          "busy": false,
          "slot": "2021-09-09T20:00:00"
        },
        {
          "busy": false,
          "slot": "2021-09-09T20:30:00"
        }
      ],
      "short_timeslots": [
        {
          "busy": false,
          "slot": "2021-09-09T08:00:00"
        },
        {
          "busy": false,
          "slot": "2021-09-09T08:30:00"
        },
        {
          "busy": false,
          "slot": "2021-09-09T09:00:00"
        },
        {
          "busy": false,
          "slot": "2021-09-09T09:30:00"
        },
        {
          "busy": false,
          "slot": "2021-09-09T10:00:00"
        },
        {
          "busy": false,
          "slot": "2021-09-09T10:30:00"
        },
        {
          "busy": false,
          "slot": "2021-09-09T11:00:00"
        },
        {
          "slot": "...",
          "buzy": false
        }
      ]
    }
  ],
  "rating": 0,
  "doctor_for": {
    "adults": true,
    "kids": false
  },
  "recommend": null,
  "educations": [
    {
      "issued_in": 1995,
      "title": "Интернатура по специальности \"Акушерство и гинекология\"",
      "issuer": "Родильный дом №2 г. Воронежа"
    },
    {
      "issued_in": 1994,
      "title": "Воронежский медицинский институт",
      "issuer": ""
    }
  ],
  "media": [
    {
      "size": 41211,
      "kind": "photo",
      "mimetype": "image\u002Fjpeg",
      "id": "0cdf0899-25ce-4925-9884-589daced7ac0",
      "title": "Фотография Панина Галина Юрьевна",
      "uri": "https:\u002F\u002Fstorage.yandexcloud.net\u002Fmedical\u002Ffiles\u002F71\u002F77\u002F7177ba5f43c0a21cfae0df770f202ce9.jpg"
    }
  ],
  "experience": 26,
  "specialties": [
    {
      "id": "5f15ca58-d9f5-4c4f-a18f-3b2f34851ddc",
      "title": "Акушер"
    },
    {
      "id": "e22989a3-d380-49fe-ba89-3dfa8c213404",
      "title": "Гинеколог"
    }
  ],
  "subways": [
    {
      "distance": 0.1,
      "line": {
        "color": "F07E24",
        "id": "5dc8ca26-029f-4e20-857b-4944c34a97c0",
        "title": "Калужско-Рижская"
      },
      "location": null,
      "id": "454b6949-4f54-4217-a1db-018b55a87ff1",
      "title": "Сухаревская",
      "slug": "suharevskaya"
    }
  ],
  "graduation": null,
  "services_count": {
    "adults": 0,
    "kids": 0
  },
  "id": "0093ce7a-85e7-47fd-9784-6e83caa60741",
  "seo": "",
  "first_name": "Галина",
  "last_modified": "2020-10-05T23:22:06.647294+03:00",
  "slug": "panina-galina-urevna-25bf",
  "services_popular": [],
  "is_active": true,
  "degree_title": null,
  "sex": "female",
  "degree": null,
  "last_name": "Панина",
  "services": [],
  "middle_name": "Юрьевна",
  "seometatags": [],
  "geoslug": {
    "subway_id": [
      "c7ffe353-f047-4604-a5bd-5bdbe1e4e399",
      "c5c16ccf-2112-4dc8-b654-508c9325531a",
      "454b6949-4f54-4217-a1db-018b55a87ff1"
    ],
    "city_district_id": [],
    "house_id": [
      "fd4a5244-98d8-493c-8ece-9f8c4c836301"
    ],
    "settlement_id": [],
    "region_id": [
      "0c5b2444-70a0-4932-980c-b4dc0d3f02b5"
    ],
    "street_id": [
      "b544c446-36fa-4556-ad66-85f596b06b27"
    ],
    "area_id": [],
    "city_id": [
      "0c5b2444-70a0-4932-980c-b4dc0d3f02b5"
    ]
  },
  "category_title": "Высшая категория",
  "partner": false,
  "price_level": "medium",
  "private__indexed_at": "2021-09-05T17:42:00.260121Z",
  "category": "high",
  "namesakes": 0,
  "services_total": 0,
  "short_specialities": "Акушер, Гинеколог",
  "url": "\u002Fmsk\u002Fdoctor\u002Fpanina-galina-urevna-25bf\u002F"
}
```

