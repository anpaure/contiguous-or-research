# Audit: exact pentagon returns for the PBBS height ladder

**Date:** 2026-08-05  
**Audited theorem:**
`MATH_THEOREM_PBBS_AH_LADDER_PENTAGON_RETURN_20260805.md`  
**Theorem SHA-256:**
`79e72e3de906f1063376ae7723d207e00afb2a987e690400be501629a82fe4a3`  
**Method:** two independent hand derivations from cyclic-parenthesis
cancellation; no finite search, code, or SAT  
**Verdict:** **PASS** for \(r\ge4\), \(2\le h<r\).

## 1. Literal-state reconstruction

Starting from

\[
 A_h=0\,1^h0^h(10)^{r-h},
\]

the forced source and target have intersection

\[
 K_h=00\,1^h0^{h+1}(10)^{r-h-1}.
\]

Removing coordinate `2` gives

\[
 L_h=000\,1^{h-1}0^{h+1}(10)^{r-h-1}.
\]

With

\[
 (z_0,z_1,c,a,z_2)=(0,1,2,2h+1,2h+2),
\]

the word factors as

\[
 0_{z_0}0_{z_1}0_c(1^{h-1}0^{h-1})0_a0_{z_2}
 (10)^{r-h-1}.
\]

The two parenthesized factors cancel completely under forward `10`
matching.  Thus the displayed five zeros are exactly the survivor set.
The five selected pairs

\[
                   23,12,01,14,34
\]

produce reduced words

\[
                   00110,01100,11000,01001,00011
\]

with respective survivors

\[
                   1,0,4,3,2.
\]

This independently recovers every forward arrow in the claimed pentagon

\[
 23\longrightarrow12\longrightarrow01\longrightarrow14
 \longrightarrow34\longrightarrow23.
\]

The first arrow expands to

\[
                  B_h\longrightarrow A_{h+1}.
\]

## 2. Reverse-survivor safety audit

For an arrow \(Z\to X=Z-x+p_+(Z)\), direct substitution in

\[
 f(Z)=Z^c-p_+(Z),\qquad f^{-1}(X)=X^c-p_-(X)
\]

shows that collision with the unchanged matching \(M_0\) occurs exactly
when \(p_-(X)=x\).

The target words, reverse survivors, and deleted labels were independently
checked as follows:

\[
\begin{array}{c|c|c}
\text{target}&p_-&\text{deleted}\\ \hline
Z_h^1&h+2&2h+1\\
Z_h^2&h+2&2\\
Z_h^3&h+2\ (h\ge3\text{ or }(h,r)=(2,3));\ 2r\ (h=2,r\ge4)&0\\
Z_h^4&h+2\ (h\ge5\text{ or }(h,r)=(4,5));\
2r\ (h=4,r\ge6);\
2r\ (h\in\{2,3\},r\ge h+2);\
0\ (h\in\{2,3\},r=h+1)&1\\
Z_h^0&h+2\ (h\ge3);\ 2r\ (h=2)&2h+2.
\end{array}
\]

The rule used here is that \(p_-\) is the zero immediately following the
rightmost global maximum of the `ones minus zeros` prefix walk.  The exact
peak comparison agrees in the interior and at every terminal case
\(h=r-1\).

No row collides for \(r\ge4\).  The only collision in the full displayed
range is the last arrow at \((r,h)=(3,2)\), where

\[
                         p_-(Z_2^0)=2r=6=z_2.
\]

The theorem excludes exactly this case.

## 3. Disjointness audit

The five state types have literal three-bit prefixes

\[
                         001,011,110,010,000.
\]

Hence different types cannot collide.  Within a type, its first long
one/zero boundary determines `h`, so different heights cannot collide.
All exchange vertices are therefore distinct over the entire bank
\(h=2,\ldots,H-1\).

The upper physical vertices are indexed injectively by \(Z\mapsto U_Z\),
and the old lower endpoints injectively by \(Z\mapsto f(Z)\).  Exchange
vertex disjointness is consequently enough for physical disjointness of
the lifted alternating ten-cycles.

## 4. Factor and support audit

Each directed pentagon is a valid alternating matching switch:

* it leaves \(M_0\) unchanged;
* it replaces five \(M_1\) slots by five new incidences;
* its first new incidence is \(I_hU_{h+1}\);
* the retained \(M_0\) incidence is \(U_hI_h\).

Thus the switches for `h=2,...,H-1` contain the alternating path

\[
 U_2-I_2-U_3-I_3-\cdots-I_{H-1}-U_H.
\]

There are \(H-2\) disjoint pentagons.  Their exact support is
\(5(H-2)\) exchange vertices.  After counting the two forced endpoints
per pentagon, the return adds \(3(H-2)\) auxiliary vertices and
\(4(H-2)\) nonforced arcs.  For \(H\le2d+1\), every quantity is
\(O(d)\).

## 5. Scope boundary

The audit validates the local two-colour PBBS factor lift and its exact
support bound.  It does not infer:

* the component derivative of the simultaneous pentagon switches;
* preservation or replacement of every downstream upper occurrence;
* extension of the protected local factor through the global compiler.

Those are correctly left open in the theorem.  The displaced-survivor
cycle-cover gate itself is closed.
