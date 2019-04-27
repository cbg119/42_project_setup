# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cbagdon <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/04/26 21:10:35 by cbagdon           #+#    #+#              #
#    Updated: 2019/04/26 21:14:45 by cbagdon          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME = test

SRC = main.c

INCLUDES = includes/

OBJECTS = $(patsubst %.c,%.o,$(SRC))

CCFLAGS = -Wall -Wextra -Werror

all: $(NAME)

$(NAME):
	make -C libft
	@gcc $(CCFLAGS) -I $(INCLUDES) -c $(addprefix src/,$(SRC))
	@mkdir build
	@mv $(OBJECTS) build
	@gcc $(CCFLAGS) -o $(NAME) $(addprefix build/,$(OBJECTS)) -L ./libft/ -lft

clean:
	make -C libft clean
	@rm -rf build

fclean: clean
	make -C libft fclean
	@rm -rf $(NAME)

re: fclean all
