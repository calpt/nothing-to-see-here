<p align="center">
    <img src="resources/adapter-bert.png" width="100"/>
</p>
<h1 align="center">AdapterHub</h1>
<h3 align="center">
    <a href="https://adapterhub.ml">Website</a>
    &nbsp; • &nbsp;
    <a href="https://docs.adapterhub.ml">Documentation</a>
    &nbsp; • &nbsp;
    <a href="https://github.com/adapter-hub/adapter-transformers">Library</a>
</h3>

You have just found _"the Hub"_, the central GitHub repository collecting all adapter modules available via the _AdapterHub_ platform.

📍 If you're here because you would like to add you own adapter to _AdapterHub_: Great! This is exactly the place to go! Refer to [our documentation](https://docs.adapterhub.ml/contributing.html) on how to get started.

🔎 If you're searching for the code of _AdapterHub_: Please go to https://github.com/adapter-hub/adapter-transformers.

❓ If you're here but don't know what all of the above is about: No problem! Check out our website at https://adapterhub.ml and our documentation at https://docs.adapterhub.ml to learn about _AdapterHub_ and to get started.

## Structure of this Repository

This repository is divided into the following subfolders:

- `TEMPLATES` contains templates for all different YAML info cards in this repository. We highly recommend you to use one of the available templates when adding your adapter, architecture, task etc. **DO NOT MODIFY ANYTHING HERE!**

- `adapter_types` contains info cards for all types of adapters supported by our framework

- `adapters` is the place where all adapter info cards should go

- `architectures` contains info cards for all available adapter architectures. Add your own architecture here!

- `dist` contains generated files for adapters and architectures. **DO NOT MODIFY ANYTHING HERE!**

- `scripts` contains script for validating the submitted adapters and info cards

- `subtasks` contains info cards for all available subtasks

- `tasks` contains info cards for all available tasks

## How To Contribute

Refer to [the step-by-step guides in our documentation](https://docs.adapterhub.ml/contributing.html) on how to contribute your adapters to the Hub.

Our [template files](https://github.com/Adapter-Hub/Hub/tree/master/TEMPLATES) are a good way to get started with any contribution to this repo.

## Citation

Please cite our paper when using _AdapterHub_ for your work:

```
@article{pfeiffer2020AdapterHub,
    title={AdapterHub: A Framework for Adapting Transformers},
    author={Jonas Pfeiffer and
            Andreas R\"uckl\'{e} and
            Clifton Poth and
            Aishwarya Kamath and
            Ivan Vuli\'{c} and
            Sebastian Ruder and
            Kyunghyun Cho and
            Iryna Gurevych},
    journal={arXiv preprint},
    year={2020},
    url={https://arxiv.org/abs/2007.07779}
}
```
