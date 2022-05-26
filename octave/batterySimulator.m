% stdin/stdout interface for simulating batteries

% DEFAULT PARAMETERS (inherited from bala demo)
k0           = -9.082;
k1           = 103.087;
k2           = -18.185;
k3           = 2.062;
k4           = -0.102;
k5           = -76.604;
k6           = 141.199;
k7           = -1.117;

Kbatt        = [k0; k1; k2; k3; k4; k5; k6; k7];

batt_model   = 3; % (1,2,3,4) battery is set to this model

Batt.Kbatt   = Kbatt;
Batt.Cbatt   = 1.9;
Batt.R0      = 0.2;
Batt.R1      = .1;
Batt.C1      = 5;
Batt.R2      = 0.3;
Batt.C2      = 500;
Batt.ModelID = batt_model;

% From here, parameters and simulation are handled by stdin

while true
    
    % read the next command

    cmd = input('','s')

    if strcmp(cmd,'quit')
        break
    end

    if strcmp(cmd, 'k')
        % get K values from stdin
        Kbatt = input('', 's');
        Kbatt = sscanf(Kbatt, '%f');
        if length(Kbatt) ~= 8
            error('Invalid input');
        end
        Batt.Kbatt   = Kbatt;
    end

end

exit;
