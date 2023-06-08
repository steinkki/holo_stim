% clear all
% close all

%%
% 
% %Load python version 3.9
% pyenv('Version', ... 
%             'C:\\Users\\stein\\anaconda3\\envs\\pymat39\\python', ... 
%             'ExecutionMode','OutOfProcess') 

%%

disp('Where are we?')  %Check the current directory, this could be a problem if we can't find the generated file.

currentDir = pwd;
disp(currentDir);

disp('Call Control notebook...')
%[status,cmdout] = 
%
%system('python progs/Engram_experiment/experimental_run.py');

pyrunfile('test_master.py')  %we can use this with Matlab versions greater then 2021b.

disp('DONE!')

%%

disp('Calling matlab output...')

folder = 'C:\Users\stein\Desktop\engram_test';  % You specify this!
fullMatFileName = fullfile(folder,  'test_true_ans.mat') %specify the name of the file, comes from the python script.
if ~exist(fullMatFileName, 'file')
  message = sprintf('%s does not exist', fullMatFileName);
  uiwait(warndlg(message));
else
  s = load(fullMatFileName);
end

disp("Matlab output loaded!")

pfft=1


