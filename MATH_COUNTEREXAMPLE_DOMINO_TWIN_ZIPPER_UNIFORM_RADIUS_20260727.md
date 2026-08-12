# Counterexample to the printed uniform domino-twin zipper theorem

Date: 2026-07-27

## 0. Verdict

Theorem 0.1 and Lemma 2.1 of
`MATH_THEOREM_DOMINO_TWIN_INVERSE_STABILITY_C_ONE_THIRD_20260727.md`
are **false as stated**.  The problem is the claimed injection

\[
 \#\{\text{released element labels}\}\le
 \#\{\text{weak cells}\}.
\]

For a fixed window radius, an anchor-free interval of cells can release
essentially **two** labels per weak cell.  The resulting family violates
the advertised bound by \(\exp(\Theta(m\sqrt{\log m}))\), even though its
defect is \(o(m)\).

This first counterexample uses fixed \(r=2\).  It therefore refutes the
printed uniform quantifier \(1<r<m-1\).  A second, stronger construction
in
`MATH_OBSTRUCTION_GLOBALLY_ALIGNED_DOUBLE_SEGMENT_DOMINO_ENTROPY_20260727.md`
also refutes every uniform exponent \(c<1/2\) in the intended annular
specialization

\[
 2r+1=m-q_0,\qquad q_0=O(\sqrt m),
\]

where \(r=(1/2-o(1))m\).  The one-segment construction below has only
exponent \(1/4+o(1)\) there, but two independently repartitioned segments
at displacement \(r\) share a remote defect front and attain exponent
\(1/2-o(1)\).  Thus an annular-only repair of the claimed \(1/3\) theorem
is impossible if it uses only raw support defect.

## 1. Construction

Let \(n=2m\), fix \(r=2\), and let

\[
 F=(B_0,B_1,\ldots,B_{m-1})
\]

be any cyclic word in disjoint unordered two-sets.  Its four-target
cells are

\[
 \mathcal S_i(F)
 =\left\{(B_i\cup B_{i+1})\cup\{x\}:
 x\in B_{i-1}\cup B_{i+2}\right\}.
\tag{1.1}
\]

Choose a cyclic interval \(I\) of \(\ell\) consecutive domino
positions, where

\[
 \ell=\left\lfloor\frac{m}{\sqrt{\log m}}\right\rfloor.
\tag{1.2}
\]

Keep every domino outside \(I\) fixed.  Repartition the \(2\ell\)
labels in the positions of \(I\) arbitrarily into an **ordered** list of
\(\ell\) unordered pairs.  Each resulting paired cyclic word defines a
simple twin packet \(G\).

The number of ordered pairings is

\[
 \frac{(2\ell)!}{2^\ell}.
\]

A simple twin support recovers its domino partition and the cyclic order
of its dominoes.  Consequently at most the dihedral group of size \(2m\)
identifies two of these words, and hence this construction produces at
least

\[
 \frac{(2\ell)!}{2^\ell(2m)}
\tag{1.3}
\]

distinct simple packets.

## 2. Defect bound

For \(r=2\), the cell \(\mathcal S_i\) depends only on the four block
positions

\[
 i-1,i,i+1,i+2.
\]

It is therefore unchanged whenever this four-position interval is
disjoint from \(I\).  Exactly at most \(\ell+3\) cell starts have a
four-position interval meeting \(I\).  Since each cell contains four
targets,

\[
 |F\setminus G|\le 4(\ell+3)=:s_m.
\tag{2.1}
\]

By (1.2), \(s_m=o(m)\).  Thus every packet in (1.3) belongs to
\(B_{s_m}(F)\).

## 3. Contradiction to exponent \(1/3\)

Stirling's formula gives

\[
 \log\frac{(2\ell)!}{2^\ell(2m)}
 =(2-o(1))\ell\log m.
\tag{3.1}
\]

On the other hand, the claimed theorem would give, for an absolute
constant \(C\),

\[
 \begin{aligned}
 \log |B_{s_m}(F)|
 &\le Cm+\frac{s_m}{3}\log n\\
 &\le Cm+\left(\frac43+o(1)\right)\ell\log m.
 \end{aligned}
\tag{3.2}
\]

The difference between (3.1) and (3.2) is

\[
 \left(\frac23-o(1)\right)\ell\log m-Cm
 =\left(\frac23-o(1)\right)m\sqrt{\log m}-Cm>0
\]

for all sufficiently large \(m\).  This contradicts (0.1).

## 4. Why this specifically refutes the release injection

The proof records the exact common subsets \(J_i\), the star/top bits,
and finitely many endpoint states.  There are only \(\exp(O(m))\) such
records.  Pigeonholing (1.3) over those records produces one fixed record
with

\[
 \exp\big((2-o(1))\ell\log m-O(m)\big)
\]

realizations.  Only the \(\ell+3\) affected cells can be weak, so the
claimed zipper injection would bound the same fibre by

\[
 C^m n^{\ell+3}
 =\exp\big((1+o(1))\ell\log m+O(m)\big),
\]

again a contradiction.  Thus the failure cannot be repaired by saying
that the exact \(J_i\)-record was omitted from the count: even after that
record is fixed, an anchor-free interval has asymptotically two released
labels per affected cell.

The sentence

> “the other member of the same domino is first encountered at the
> paired front ... and is assigned there unless already forced”

does not show that the mate is forced.  It merely moves its first
occurrence to another front.  For fixed \(r\), that other front remains
inside the same anchor-free interval, and both labels remain free.

## 5. What the one-segment mechanism does in the annular regime

For a general radius \(r\), a contiguous \(\ell\)-block modification can
affect up to \(2\ell+O(1)\) cells when

\[
 \ell<\min(r,m-r)-2.
\]

It then has defect at most \(8\ell+O(1)\), while (1.3) has logarithm
\((2-o(1))\ell\log m\).  This is the known lower list exponent

\[
 \frac{2\ell}{8\ell}=\frac14.
\]

Hence this *single-segment* construction does not contradict an annular
estimate with exponent \(1/3\).  It is not the extremal annular family.

Put

\[
 h=m-2r=q_0+1=\Theta(\sqrt m).
\]

Take two independently repartitioned length-\(\ell\) segments \(I\) and
\(I+r\).  Their four nominal core fronts collapse to three bands

\[
 L,\quad L-r,\quad L+r,
\]

and the last two are separated by only \(h\), since
\(2r\equiv-h\pmod m\).  The number of possibly changed cells is at most

\[
 2(\ell-1)+\min\{\ell-1,h\}+4,
\]

while the family has at least

\[
 \frac1{2m}\left(\frac{(2\ell)!}{2^\ell}\right)^2
\]

simple supports.  At \(\ell=m/\sqrt{\log m}\), this gives defect
\(s\le8\ell+4h+O(1)=o(m)\) and list exponent \(1/2-o(1)\).  The
logarithmic family size is \(\Theta(m\sqrt{\log m})\), so no
\(\exp(O(m))\) prefactor repairs a bound with any fixed \(c<1/2\).

This identifies the exact failure of a proposed carrier-gap decoder:
opposite-front anchoring is not independent for the two segments.  The
remote fronts overlap on all but an \(O(h)\) fringe.

## 6. Audit of the top-cell carrier-gap decoder

There is also a literal local failure at a two-point anchor, even before
the double-segment obstruction is used.  Let \(A\) be an \(F\)-star core
and choose one label \(u\) from its left boundary domino and one label
\(v\) from its right boundary domino.  Put

\[
 X=A\cup\{u\},\qquad Y=A\cup\{v\},\qquad U=A\cup\{u,v\}.
\]

Declare \(\{X,Y\}\) to be top-phase in \(G\).  For any distinct
\(p,q\in A\), take the endpoint dominoes

\[
 P=\{u,p\},\qquad Q=\{v,q\},
\]

and pair \(A\setminus\{p,q\}\) internally.  The \(r+1\) consecutive
dominoes from \(P\) to \(Q\) have union \(U\), and their top cell
contains the same prescribed edge \(\{X,Y\}\).  No \(G\)-star contains
both \(X,Y\): such a star would have core \(A\), but \(A\) is not a
union of \(r\) of these \(G\)-dominoes.  Thus this is genuinely top-only.

The carrier \(U\), common edge, and phase are identical for all
\(\binom{R-1}{2}=\Theta(n^2)\) choices of \(\{p,q\}\).  The immediate
two-star collar can be completed so that it has exactly the two common
targets \(X,Y\), and hence six targets in \(G\setminus F\).  Therefore a
top-only anchor releases two labels and has the sharp local charge

\[
 2\text{ free labels}/6\text{ defects}=1/3.
\]

This directly refutes the zipper table's row
\(k=2\Rightarrow0\) free labels.  A *deferred-mate* decoder can repair the
local row by assigning each free mate to a neighbouring one-common-target
star cell, thereby charging three new targets per mate.  However, that
local repair cannot prove the global inverse theorem: in the double-
segment family the deferred collars from the two segments reuse the same
remote front.  The charge is therefore not additive.

## 7. Exact status

* **Refuted:** uniform inverse stability for all \(1<r<m-1\); the stated
  paired-window zipper Lemma 2.1; the asserted general one-release-per-
  weak-cell injection.
* **Refuted in the annular regime:** every uniform raw-defect list bound
  \(\exp(O(m))n^{cs}\) with fixed \(c<1/2\), including \(c=1/3\).
* **Still open:** a terminal-scale estimate at
  \(s=A m/\log m\) with an explicit additive exponential constant, or a
  trajectory/cluster theorem which prevents the two \(r\)-separated
  repartitions from surviving independently.
