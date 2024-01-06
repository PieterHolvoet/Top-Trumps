-- FUNCTION: public.get_computer_choice(integer, character varying, character varying)

-- DROP FUNCTION IF EXISTS public.get_computer_choice(integer, character varying, character varying);

CREATE OR REPLACE FUNCTION public.get_computer_choice(
	p_id integer,
	p_difficulty character varying,
	p_round_type character varying)
    RETURNS character varying
    LANGUAGE 'plpgsql'
    COST 100
    VOLATILE PARALLEL UNSAFE
AS $BODY$
DECLARE
    choice_column VARCHAR;
    result_value VARCHAR;
BEGIN
    -- Determine the column based on difficulty and round type
    IF p_difficulty = 'Easy' THEN
        IF p_round_type = 'Higher' THEN
            choice_column := 'HigherChoiceEasy';
        ELSE
            choice_column := 'LowerChoiceEasy';
        END IF;
    ELSIF p_difficulty = 'Medium' THEN
        IF p_round_type = 'Higher' THEN
            choice_column := 'HigherChoiceMedium';
        ELSE
            choice_column := 'LowerChoiceMedium';
        END IF;
    ELSE
        -- Assuming Hard mode
        IF p_round_type = 'Higher' THEN
            choice_column := 'HigherChoiceHard';
        ELSE
            choice_column := 'LowerChoiceHard';
        END IF;
    END IF;

    -- Use dynamic SQL to fetch the corresponding choice data from opponent_choices
    EXECUTE 'SELECT ' || quote_ident(choice_column) || ' FROM opponent_choices WHERE choice_id = $1'
    INTO result_value
    USING p_id;

    -- Return the result without brackets
    RETURN result_value;
END;
$BODY$;

ALTER FUNCTION public.get_computer_choice(integer, character varying, character varying)
    OWNER TO postgres;