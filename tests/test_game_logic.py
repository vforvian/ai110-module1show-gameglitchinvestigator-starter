from logic_utils import check_guess, parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)    #FIXME: check_guess returns (outcome, message)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)    #FIXME: check_guess returns (outcome, message)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)    #FIXME: check_guess returns (outcome, message)
    assert outcome == "Too Low"

def test_too_high_says_go_lower():
    # A guess above the secret should tell the player to go LOWER
    outcome, message = check_guess(100, 50)
    assert "LOWER" in message

def test_too_low_says_go_higher():
    # A guess below the secret should tell the player to go HIGHER
    outcome, message = check_guess(1, 50)
    assert "HIGHER" in message

def test_hint_compares_numbers_not_text():
    # As text, "9" > "50", but as numbers 9 < 50, so this should be "Too Low"
    outcome, message = check_guess(9, 50)
    assert outcome == "Too Low"

def test_guess_in_range_is_accepted():
    # Both ends of the range are valid guesses
    assert parse_guess("1", 1, 100) == (True, 1, None)
    assert parse_guess("100", 1, 100) == (True, 100, None)

def test_negative_guess_is_rejected():
    # A negative number is below the range
    ok, value, err = parse_guess("-5", 1, 100)
    assert ok is False
    assert err == "Guess must be between 1 and 100."

def test_guess_above_range_is_rejected():
    # 101 is above the Normal range of 1-100
    ok, value, err = parse_guess("101", 1, 100)
    assert ok is False

def test_range_follows_difficulty():
    # 21 is fine on Normal (1-100) but out of range on Easy (1-20)
    ok_normal, _, _ = parse_guess("21", 1, 100)
    ok_easy, _, _ = parse_guess("21", 1, 20)
    assert ok_normal is True
    assert ok_easy is False

def test_non_number_is_rejected():
    ok, value, err = parse_guess("abc", 1, 100)
    assert ok is False
    assert err == "That is not a number."
