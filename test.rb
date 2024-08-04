require 'pry'

new_game

class BlackjackGame
  SUITS = %i[spades hearts diamonds clubs]
  VALUES = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  GAME_STATUS = {
    win: :win,
    lose: :lose,
    bust: :bust,
    draw: :draw
  }

  attr_reader :cards, :player_hand, :dealer_hand

  def initialize
    @cards = shuffle_decks
    @player_hand = []
    @dealer_hand = []
  end

  def shuffle_decks
    # Shuffle the deck... (Implementation left to the reader)
    # For simplicity, we will just use a pre-shuffled deck for now
    VALUES.dup.shuffle + VALUES.dup.shuffle
  end

  def deal_card
    cards.pop
  end

  def deal_initial_cards
    2.times { player_hand << deal_card }
    2.times { dealer_hand << deal_card }
  end

  # rest of the methods (hit, stand, calculate_score, etc.)
 end

 def new_game
  game = BlackjackGame.new
  game.deal_initial_cards
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_hand = []
    dealer_hand = []
    player_score = 0
    dealer_score = 0

    def deal_card
      cards.sample
    end

    def calculate_score(hand)
      score = hand.reduce(:+)
      if score > 21 && hand.include?(11)
        hand[hand.index(11)] = 1
        score = hand.reduce(:+)
      end
      score
    end

    2.times { player_hand << deal_card }
    2.times { dealer_hand << deal_card }

    puts "Dealer's cards: #{dealer_hand[0]} Total score: #{dealer_hand[0]}"
    puts "Player's cards: #{player_hand} Total score: #{calculate_score(player_hand)}"

    play_again = true
    while play_again
      if calculate_score(player_hand) < 21
        hit = gets.chomp
        if hit == 'y'
          player_hand << deal_card
          puts "Player's cards: #{player_hand} Total score: #{calculate_score(player_hand)}"
        else
          play_again = false
        end
      else
        play_again = false
      end
    end

    while calculate_score(dealer_hand) < 17
      dealer_hand << deal_card
    end

    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)

    puts "Dealer's cards: #{dealer_hand} Total score: #{dealer_score}"
    puts "Player's cards: #{player_hand} Total score: #{player_score}"

    case
    when player_score > 21 then puts "You Bust! You Lose!"
    when dealer_score > 21 then puts "Dealer Busts! You Win!"
    when player_score > dealer_score then puts "You Win!"
    when player_score < dealer_score then puts "You Lose!"
    else puts "It's a draw!"
    end

    play_again = gets.chomp
    if play_again == 'y'
      new_game
    else
      puts "Goodbye!"
      exit
    end
  end

 new_game
