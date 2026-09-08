# Audit of the one-shell triangular braid

## Verdict

**PASS for the local shell, residual, separator, and sparse-lift theorems.**

The proposed word spans the triangular alphabet with exactly `R-2` repeated
occurrences and its missing targets are exactly the stated affine strict
triangle.  The separator word represents every target crossing its chosen
cut, and the sparse two-level lift has zero alphabet-inventory loss.

This does **not** prove a new recurrence for the repetition excess.  The
quantity `chi_R` packages the still-missing global ordering theorem.  No
bound `chi_R=o(R)`—or even a nontrivial uniform improvement over the known
linear per-level cost—is supplied.  Consequently no four-box or global
asymptotic constant changes.

The displayed length formula should be stated for `R>=2`; the `R=1`
degenerate word is harmless but does not satisfy the literal `R-2` excess
expression.

## 1. Exact shell

Let

\[
 T_R=\{P_0\}\cup\{E_{s,y}:1\le s\le R,\ 0\le y<s\}.
\]

The outer fan has `2R` occurrences.  The block of row `s` in the linked
shell has `s` occurrences, so

\[
 |S_R|=2R+\sum_{s=2}^{R-1}s
      ={R^2+3R-2\over2}
      =|T_R|+R-2.
\]

The outer fan supplies the complete top row and every peak.  The linked
shell supplies every positive-height cell in rows `2,...,R-1`; hence the
word spans `T_R`.

The five proposed witness classes are correct:

1. `r=R` uses a suffix of the top row followed by descending peaks;
2. `x=0` uses the descending peak interval;
3. `u=0` crosses from the peak interval into the initial shell blocks;
4. `u=r-1` uses the start of shell block `r`; and
5. `1<=u<=r-2`, `x>=r-2` crosses complete intermediate shell blocks.

Their complement is exactly

\[
 M_R=\{(u,r,x):4\le r\le R-1,\ 1\le u\le r-2,
                         \ 1\le x\le r-3\}.
\]

No member of `M_R` can use the outer fan: positive height there forces row
`R`, while avoiding row `R` leaves only peaks.  A crossing into the linked
shell either retains row `R` or passes through `P_0`.  Inside the shell, an
interval with minimum row `u<=r-2` and maximum row `r` must cross the entire
`(r-1)` block, including `E_(r-1,r-2)`.  Its maximum height is therefore at
least `r-2`, excluding precisely `x<=r-3`.

## 2. Residual triangle

The affine change

\[
 (u',r',x')=(u-1,r-2,x-1)
\]

is a bijection from `M_R` to

\[
 0\le u'<r'\le R-3,\qquad0\le x'\le r'-2.
\]

Thus the missing family is one strict triangular target set with its top
height face removed.  This is a genuine simplification of the local target
ledger.

## 3. Separator portals

For `u>=1`, put

\[
 L_{u,x}=E_{u,\min(x,u-1)},
\]

and put `L_(0,x)=P_0`.  In the word

\[
 L_{a,x},\ldots,L_{t,x},P_t,
 E_{q,x},E_{q+1,x},\ldots,E_{b,x},
 \qquad q=\max(t+1,x+1),
\]

the interval from `L_(u,x)` to `E_(r,x)` is legal whenever
`a<=u<=t<r<=b` and `x<r`.  Its first-coordinate extrema are `u,r`; the
portal supplies height zero; the right endpoint supplies height `x`; and
every intermediate cell lies in the desired rectangle.  The separator
theorem is therefore exact.

A balanced interval tree assigns every pair `u<r` to one crossing
separator.  Literal concatenation of all resulting height-specific gadgets,
however, repeats their provider chains heavily.  The tree is a coverage
decomposition, not the missing economical linearization.

## 4. Sparse lift and recurrence scope

The lift

\[
 P_s\mapsto P_{s+2},\qquad E_{s,y}\mapsto E_{s+2,y+2}\ (y\ge1)
\]

omits exactly

\[
 \{P_0,P_1\}\cup\{E_{s,1}:2\le s\le R\}
 \cup\{E_{s,2}:3\le s\le R\},
\]

which has `2R-1=|T_R|-|T_(R-2)|` cells.  Peaks remain peaks, while positive
heights increase by two, so the stated target transfer is exact.

Consequently, lifting a word of excess `rho(R-2)` and adjoining every omitted
cell once produces a multiset of size `|T_R|+rho(R-2)`.  Defining `chi_R` as
the extra cost needed to order/superpose that multiset with all lifted,
shell, separator, and merge-forest constraints makes

\[
 \rho(R)\le\rho(R-2)+\chi_R
\]

true by definition.  The substantive theorem would be
`chi_R=O(R^(1-epsilon))`; it remains unproved.  In particular, local
range-maximum validity does not by itself construct the global merge-forest
splicing or coordinate pins.

For the shell words themselves there is a sharper exact multiset identity:

\[
 S_R=\Sigma_R(S_{R-2})\uplus(\text{all omitted cells})
                         \uplus\{P_1,P_2\}.          \tag{4.1}
\]

Indeed, `S_R` contains every peak `P_1,...,P_(R-2)` twice.  The lifted shell
already contains `P_3,...,P_(R-2)` twice, while `P_1,P_2` occur only once
after adjoining the omitted alphabet.  All other multiplicities agree.
Thus the shell inventory itself costs only two new occurrences per two-level
step.  This does not solve the recurrence: inserting the omitted `P_0,P_1`
between the lifted outer fan and lifted shell contaminates precisely the
lifted witnesses that cross that seam.  Preserving or replacing those
crossing witnesses, together with the separator family, is the ordering
problem measured by `chi_R`.

## 5. Exhaustive regression

The independent checker

```text
scratch/audit_triangular_one_shell.py
```

enumerates every interval of the shell through `R=20`, checks exact equality
of the missing family and the affine residual, verifies the sparse-lift
inventory, and checks every separator gadget through `R=15`.  It reports

```text
PASS: shell/lift R<=20; separator gadgets R<=15
```

Its SHA-256 is

```text
c64c5a1f4a4cfe7392190d9ef9d595875ca7e97df69b2c58bb0d019c16acf1a0
```
