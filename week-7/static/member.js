const userSearchForm = document.querySelector('.search-user')

// 查詢會員姓名
function searchUser(find){
    find.preventDefault()
    const search = this.querySelector('input').value
    const searchResult = this.querySelector('p')
    let url = `/api/members?username=${search}`
    fetch(url)
        .then(res => res.json())
        .then(data => {
            const name = data['data']['name']
            const username = data['data']['username']
            searchResult.innerText = `${name}(${username})`
        })
}



userSearchForm.addEventListener('submit', searchUser)
