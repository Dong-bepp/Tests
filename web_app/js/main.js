document.getElementById('loginForm').addEventListener('submit', function(e) {
    e.preventDefault(); // 阻止表单默认提交刷新页面
    const user = document.getElementById('username').value;
    const pass = document.getElementById('password').value;

    // 模拟登录逻辑：用户名admin，密码123456
    if (user === 'admin' && pass === '123456') {
        document.getElementById('message').style.color = 'green';
        document.getElementById('message').innerText = '登录成功！欢迎, ' + user;
    } else {
        document.getElementById('message').style.color = 'red';
        document.getElementById('message').innerText = '登录失败：用户名或密码错误 (试试 admin/123456)';
    }
});

function searchBook() {
    const query = document.getElementById('searchBox').value;
    const resultsList = document.getElementById('results');
    resultsList.innerHTML = ''; // 清空旧结果

    if (query.toLowerCase().includes('算法')) {
        resultsList.innerHTML += '<li>《算法导论》 - Thomas H.Cormen - ¥45.00</li>';
    }
    if (query.toLowerCase().includes('设计')) {
        resultsList.innerHTML += '<li>《设计模式》 - GoF - ¥30.00</li>';
    }
    if (resultsList.innerHTML === '') {
        resultsList.innerHTML = '<li>未找到相关书籍</li>';
    }
}