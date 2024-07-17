fetch("https://api.talkdeskapp.com/virtual-agent/monitor/conversations/session/117ab2be-0835-42a1-8303-f0811eefb6c3", {
    "headers": {
        "accept": "application/json, text/plain, */*",
        "accept-language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
        "authorization": "Bearer eyJraWQiOiIxYWI2YjBhNjAxNTY0MmY4YjA5MWM3MjE1MWIxMGQ5MCIsImFsZyI6IkVTMjU2In0.eyJpc3MiOiJodHRwczovL3d3dy50YWxrZGVza2lkLmNvbSIsImF1ZCI6Imh0dHBzOi8vYXBpLnRhbGtkZXNrYXBwLmNvbSIsImV4cCI6MTcyMTIxODg2NiwibmJmIjoxNzIxMjE4MjY2LCJpYXQiOjE3MjEyMTgyNjYsImp0aSI6ImI1YzNiNmQyMjEwNjRkMzg4YWQ3MGIyZGZiYmUzMjg5IiwiY2lkIjoiZTk5OWJjNzZlYTQyNDc4MmFkMzU0MWIyOGE3M2FmYzIiLCJndHkiOiJyZWZyZXNoX3Rva2VuIiwic2NwIjpbImFjY291bnQ6cmVhZCIsImFjdGlvbnM6cmVhZCIsImdyYXBoLXVzZXJzOnJlYWQiLCJvcGVuaWQiLCJ1c2VyLXJpbmctZ3JvdXBzOnJlYWQiLCJ1c2VyLXJvbGVzOnJlYWQiLCJ1c2VyczpyZWFkIiwidmlydHVhbC1hZ2VudC1tb25pdG9yOnJlYWQiLCJ2aXJ0dWFsLWFnZW50LW92ZXJ2aWV3OnJlYWQtc3RhdHMiLCJ2aXJ0dWFsLWFnZW50cy1mbG93cy1jb25maWc6cmVhZCIsInZpcnR1YWwtYWdlbnRzLWZsb3dzLWNvbmZpZzp3cml0ZSIsInZpcnR1YWwtYWdlbnRzLWZsb3dzLWNvbnRlbnQ6cmVhZCIsInZpcnR1YWwtYWdlbnRzLWZsb3dzLWNvbnRlbnQ6d3JpdGUiLCJ2aXJ0dWFsLWFnZW50cy1mbG93czpyZWFkIiwidmlydHVhbC1hZ2VudHMtZmxvd3M6d3JpdGUiXSwicmxtIjoiTUFJTiIsImFpZCI6IjY1ZTc5ZjJhNzQyYjAzMTY5YTU5NzQ1OSIsImFjYyI6ImpvYmhvbWVuaW9kaWdpdGFsIiwicHNuIjoiSU5URVJOQUwiLCJyZWciOiJ1cy1lYXN0LTEiLCJzdWIiOiJjMjY3OWFhNTZlYjk0ZTllYjY0NmMyOWE3MTkyYmVkOCIsInVzciI6ImVkeS5hbHZlc0Bqb2Job21lLmNvbS5iciIsInVpZCI6IjY1ZTc5ZjJkZmM4NDVjNjg0N2E3MDNiYiIsInNpZCI6IjIyODQ1ZTUwNTkyZjQyYmU5ZjRkOGE3ZmUwYTg3MjFjIn0.SCTdVH-EHhwjnDqhStyNittPKS_0YzsLUeW8WXqZj001HyfKZ4FfZ-DV5okWi508fAyecG_HSnUb8bFcoa4ezg",
        "priority": "u=1, i",
        "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Linux\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "Referer": "https://prd-cdn-talkdesk.talkdesk.com/",
        "Referrer-Policy": "strict-origin-when-cross-origin"
    },
    "body": null,
    "method": "GET"
})
    .then(response => response.json())
    .then(console.log.bind(console));