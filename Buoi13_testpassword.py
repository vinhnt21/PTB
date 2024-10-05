'''
1. Độ dài >= 8 ký tự    +1
2. Có ít nhất 1 chữ cái viết hoa   +1
3. Có ít nhất 1 chữ cái viết thường   +1
4. Có ít nhất 1 số   +1
5. Có ít nhất 1 ký tự đặc biệt   +1
'''


def test_password(password:str) -> int:
    score = 0
    if len(password) >= 8:
        score += 1
        
    is_contain_upper = False
    for c in password:
        if c.isupper():
            is_contain_upper = True
            break
    if is_contain_upper:
        score += 1
        
        
    is_contain_lower = False
    for c in password:
        if c.islower():
            is_contain_lower = True
            break
    if is_contain_lower:
        score += 1
        
    is_contain_digit = False
    for c in password:
        if c.isdigit():
            is_contain_digit = True
            break
    if is_contain_digit:
        score += 1
    
    is_contain_special = False
    for c in password:
        if not c.isalnum():
            is_contain_special = True
            break
    if is_contain_special:
        score += 1
    
    return score

def show_password_score(password:str) -> None:
    score = test_password(password)
    print(f"Điểm số của mật khẩu {password} là: {score}")
    
show_password_score("12345678")
show_password_score("12345678a")
show_password_score("12345678A")
show_password_score("12345678Aa")
show_password_score("12345678Aa@")

        
        
    
    