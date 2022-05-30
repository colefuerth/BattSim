% stdin/stdout interface for simulating batteries

% DEFAULT PARAMETERS (inherited from bala demo)
k0 = -9.082;
k1 = 103.087;
k2 = -18.185;
k3 = 2.062;
k4 = -0.102;
k5 = -76.604;
k6 = 141.199;
k7 = -1.117;

Kbatt = [k0; k1; k2; k3; k4; k5; k6; k7];

batt_model = 3; % (1,2,3,4) battery is set to this model

Batt.Kbatt = Kbatt;
Batt.Cbatt = 1.9;
Batt.R0 = 0.2;
Batt.R1 = .1;
Batt.C1 = 5;
Batt.R2 = 0.3;
Batt.C2 = 500;
Batt.ModelID = batt_model;

%current simulation parameters
delta = 100*10^(-3);
Tc  = 10;  % sampling
D   = 100; % duration of the simulation
Id = -500; % amplitude of current (mA)

Batt.alpha1 = exp(-(delta/(Batt.R1*Batt.C1)));
Batt.alpha2 = exp(-(delta/(Batt.R2*Batt.C2)));

%current simulation
[T,I] = CurretSIM('rectangularnew',-Id, Id, delta, Tc, D);


% From here, parameters and simulation are handled by stdin

while true

    % read the next command

    cmd = input('', 's');

    if strcmp(cmd, 'quit')
        break
    end

    if strcmp(cmd, 'k')
        % get K values from stdin
        Kbatt = input('', 's');
        Kbatt = sscanf(Kbatt, '%f');

        if length(Kbatt) ~= 8
            error('Invalid input, syntax is {k0 k1 k2 k3 k4 k5 k6 k7}');
        end

        Batt.Kbatt = Kbatt;
        disp('done');
    end

    if strcmp(cmd, 'c')
        % get C values from stdin
        Cbatt = input('', 's');
        Cbatt = sscanf(Cbatt, '%f');

        if length(Cbatt) ~= 3
            error('Invalid input, syntax is {Cbatt C0 C1}');
        end

        Batt.Cbatt = Cbatt(1);
        Batt.C0 = Cbatt(2);
        Batt.C1 = Cbatt(3);
        disp('done');
    end

    if strcmp(cmd, 'r')
        % get R values from stdin
        Rbatt = input('', 's');
        Rbatt = sscanf(Rbatt, '%f');

        if length(Rbatt) ~= 3
            error('Invalid input, syntax is {Rbatt R0 R1}');
        end

        Batt.R0 = Rbatt(1);
        Batt.R1 = Rbatt(2);
        Batt.R2 = Rbatt(3);
        disp('done');
    end

    if strcmp(cmd, 'm')
        % get model ID from stdin
        Batt.ModelID = input('', 's');

        if length(Batt.ModelID) ~= 1
            error('Invalid input, syntax is {modelID}');
        end

        Batt.ModelID = str2double(Batt.ModelID);
        disp('done');
    end

    if strcmp(cmd, 'cs')
        %  use CurretSIM to generate the simulation profile

        temp = input('', 's');
        shape = strtrim(temp); % remove the \n at the end
        temp = input('', 's');
        Id = sscanf(temp, '%f');
        temp = input('', 's');
        Tc = sscanf(temp, '%f');
        temp = input('', 's');
        D = sscanf(temp, '%f');
        [T,I] = CurretSIM(shape, -Id, Id, delta, Tc, D);
        disp('done');

    end

    if strcmp(cmd, 'ms')
        %  manually set the simulation profile
        % I is a vector of current values
        I = input('', 's');
        I = sscanf(I, '%f');

        % T is a vector of time values, corresponding to I
        T = input('', 's');
        T = sscanf(T, '%f');
    end


    if strcmp(cmd, 's')
        % simulate battery

        % signal noise
        SNR = 50;
        sigma_i = 0; % current measurement noise
        sigma_v = 10^(-SNR / 20); % voltage measurement noise

        delta = 100 * 10^(-3);

        [Vbatt, Ibatt, ~, Vo] = battSIM(I, T, Batt, sigma_i, sigma_v, delta);

        % output the results
        fprintf('%f ', Vbatt);
        fprintf('\n');
        fprintf('%f ', Ibatt);
        fprintf('\n');
        fprintf('%f ', Vo);
        fprintf('\n');
        disp('done');
    end

end

exit;
