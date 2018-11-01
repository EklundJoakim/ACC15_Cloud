% Copyright (c) 2015, BENCHOP, Slobodan Milovanović
% All rights reserved.
% This MATLAB code has been written for the BENCHOP project.
% Redistribution and use in source and binary forms, with or without
% modification, are permitted provided that the following conditions are
% met:
%    * Redistributions of source code must retain the above copyright
%       notice, this list of conditions and the following disclaimer.
%    * Redistributions in binary form must reproduce the above copyright
%       notice, this list of conditions and the following disclaimer in
%       the documentation and/or other materials provided with the distribution
%    * BENCHOP article is properly cited by the user of the BENCHOP codes when publishing/reporting related scientific results.
% 
% THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
% AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
% IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
% ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
% LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
% CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
% SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
% INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
% CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
% ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
% POSSIBILITY OF SUCH DAMAGE.


function [result] = Table(number, r)

format long
warning off

%% Problem 1 a) I
if number==1 
    rootpath=pwd;
    S=[90,100,110]; K=100; T=1.0; sig=0.15; %r=0.03; 
    U=[2.758443856146076 7.485087593912603 14.702019669720769];

    filepathsBSeuCallUI=getfilenames('./','BSeuCallUI_*.m');
    par={S,K,T,r,sig};
    [timeBSeuCallUI,relerrBSeuCallUI] = executor(rootpath,filepathsBSeuCallUI,U,par);
    
    time = timeBSeuCallUI;
    relError = relerrBSeuCallUI;
    problem = 'Black–Scholes–Merton model for one underlying asset';
   
    result = [time, relError];
    cd(rootpath);
     
%% Problem 1 b) I
elseif number==2 
    rootpath=pwd;
    S=[90,100,110]; K=100; T=1.0; sig=0.15; %r=0.03; 
    U=[10.726486710094511 4.820608184813253 1.828207584020458];
    
    filepathsBSamPutUI=getfilenames('./','BSamPutUI_*.m');
    par={S,K,T,r,sig};
    [timeBSamPutUI,relerrBSamPutUI] = executor(rootpath,filepathsBSamPutUI,U,par);
    
    time = timeBSamPutUI;
    relError = relerrBSamPutUI;
    problem = 'Black Scholes Merton model with discrete dividends';
    result = [time, relError];
    cd(rootpath);

%% Problem 1 c) I
elseif number==3
    rootpath=pwd;
    S=[90,100,110]; K=100; T=1.0; B=1.25*K; sig=0.15; %r=0.03;
    U=[1.822512255945242 3.294086516281595 3.221591131246868];
    
    filepathsBSupoutCallI=getfilenames('./','BSupoutCallI_*.m');
    par={S,K,T,r,sig,B};
    [timeBSupoutCallI,relerrBSupoutCallI] = executor(rootpath,filepathsBSupoutCallI,U,par);
    
    time = timeBSupoutCallI;
    relError = relerrBSupoutCallI;
    problem = 'Black Scholes Merton model with local volatility';
    result = [time, relError];
    cd(rootpath);
end

end
