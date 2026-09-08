# Correction map: six-slot `h=4` literal rectangle correlated gate

**Date:** 2026-08-04  
**Status:** packaging-only successor map responding exactly to the
independent fail-closed audit.  No rectangle identity, inequality,
constant, far-end margin, or KKT equation has changed.

## 1. Lineage

| role | SHA-256 |
|---|---|
| predecessor theorem | `a8498766b53880fc4490626627c187a329e2ed4f448853e347e2160f2d573924` |
| independent packaging audit | `ba3e903140a54bdd24ad9c2af1d486030474b01fe6bc1c0f3a09fd0529fd5deb` |
| corrected successor theorem | `533f194ed727b2c15d26ca2007131a3bfc22f08f401097f74d021d40cf5dd5cd` |

The predecessor is superseded and must not be cited as independently GO.

## 2. Exact correction 1: display escape

The malformed plain tokens

\[
                         0,quad u,quad P,quad P+u
\]

were replaced by the intended TeX

\[
                         0,\quad u,\quad P,\quad P+u.
\]

## 3. Exact correction 2: self-audit denominator conversion

The theorem's arithmetic was already correct.  Its self-audit incorrectly
converted two fractions to denominator `700000`.  The corrected line is

\[
 {1\over20000}+{1129\over25000}-{57\over1400}
 ={35+31612-28500\over700000}
 ={3147\over700000}.
\]

## 4. Exact correction 3: local-interval dependency binding

The rectangle theorem invokes positivity through

\[
 \delta_*={43849\over643260}.
\]

Its dependency table and successor freeze now bind explicitly to:

* corrected local theorem
  `badc46480b85ef794e784ca2f62273aa6258cdf3dcfecbd915553102c6acd6af`;
* final independent GO audit
  `5781c83357c77dd8216ecbb24ab4739e779d0c65751c7f8aecce1ef43b6ae46c`.

No stale `340570...` predecessor is part of the successor proof chain.

## 5. Unchanged substantive rows

The independent audit explicitly passes:

1. the physical rectangle `0,u,P,P+u`;
2. the correlated `y,z` charge
   `Gamma(delta)<3147/700000`;
3. exact endpoint elimination of `x`;
4. `Phi>mathfrak R` and the strict counterexample implication;
5. the far-end margin `23453/700000` and uniform neighborhood argument;
6. both smooth KKT systems and the complete boundary/switch list.

Only the three packaging rows above changed in the successor.
