# Kneser critical rounding: endpoint anticodes and the isolated correlation gate

Date: 2026-07-26

Method: pure mathematics, using the Ahlswede--Khachatrian Complete
Intersection Theorem and the standard hypergeometric Hoeffding bound.

## 0. Verdict

The logarithmic augmenter inventory found in
MATH_THEOREM_KNESER_ZERO_SIGNATURE_HEXAGON_AND_CRITICAL_AUGMENTER_20260726.md
does **not** admit a size-only endpoint supersaturation theorem.  For every
\(L=o(\sqrt m)\), there are \(L\)-intersecting families of
\((m-1)\)-sets of density \(1/2-o(1)\).  In particular, a Catalan-size
leave can contain no endpoint pair with intersection at most
\(\log m+3\log\log m\).

There is nevertheless a sharp deterministic replacement.  Put

\[
 T_\star=\left\lceil
   \sqrt{2(m-1)\log(2m)}
 \right\rceil.                                                \tag{0.1}
\]

Every leave \(\mathcal U\subseteq\binom{[2m]}{m-1}\) of size \(u\)
contains a matching of at least

\[
                         {u-D/2\over2}                         \tag{0.2}
\]

disjoint endpoint pairs \(R,S\) satisfying
\(|R\cap S|<T_\star\).  Thus endpoint supply is completely deterministic
at the Gaussian anticode scale.

The genuinely open input can then be isolated as one conditional moment.
For each endpoint pair use the exact all-intersection augmenter of the
companion note.  If the actual count of templates whose prescribed old
edges lie in the current matching and whose two terminal owner pairs have
a free clone is at least an \(e^{-o(m)}\) fraction of its natural
edge-density benchmark, then an augmenter exists.  The benchmark is
exponentially large:

\[
             \exp\bigl((2\log2-o(1))m\bigr).                  \tag{0.3}
\]

Hence no polynomial or subexponential precision is required.  The only
remaining owner-rounding issue is the possibility of an
\(\exp(-\Theta(m))\) adversarial correlation between

* the leave;
* logarithmic/Gaussian-length prescribed old paths; and
* the two free terminal clones.

This is stronger separation than the original critical-rounding gate:
endpoint geometry and all arithmetic are proved; only the joint
old-edge/free-clone correlation remains.  The separate owner-cycle gate
still requires availability of the exact zero-signature hexagons.

## 1. The logarithmic endpoint statement is false

Let \(L=L(m)=o(\sqrt m)\), choose \(B\subset[2m]\) with \(|B|=m\), and
put

\[
 a=\left\lceil{m+L+1\over2}\right\rceil,
\qquad
 \mathcal V_L=
 \left\{R\in\binom{[2m]}{m-1}:|R\cap B|\ge a\right\}.         \tag{1.1}
\]

### Proposition 1.1 (dense anticode obstruction)

Every two members of \(\mathcal V_L\) intersect in at least \(L+1\)
points, while

\[
                     |\mathcal V_L|
                     =\left({1\over2}-o(1)\right)N.           \tag{1.2}
\]

Consequently, for every fixed \(C\) and all sufficiently large \(m\),
there is a subfamily of \(\mathcal V_L\) of size \(CD\) containing no pair
with intersection at most \(L\).

#### Proof

For \(R,S\in\mathcal V_L\),

\[
 |R\cap S|
 \ge |R\cap S\cap B|
 \ge |R\cap B|+|S\cap B|-|B|
 \ge2a-m\ge L+1.                                             \tag{1.3}
\]

For uniform \(R\in\binom{[2m]}{m-1}\), the variable
\(X=|R\cap B|\) has mass function

\[
 \Pr(X=j)
 ={ \binom mj\binom m{m-1-j}\over N}
 ={ \binom mj\binom m{j+1}\over N}.                          \tag{1.4}
\]

It is symmetric under \(j\leftrightarrow m-1-j\).  Stirling's formula
gives \(\max_j\Pr(X=j)=O(m^{-1/2})\).  The interval between the symmetry
centre \((m-1)/2\) and the threshold \(a\) has \(O(L+1)\) atoms and
therefore mass \(o(1)\).  Symmetry now gives (1.2).  Finally
\(CD/N=C/m=o(1)\), so the required subfamily exists. \(\square\)

This proposition rules out any attempt to prove the logarithmic endpoint
part from the cardinality of the leave alone.  A matching-specific
anti-clustering theorem could still make the logarithmic route work, but
that would itself be an additional correlation theorem.

## 2. Deterministic endpoint packing at the Gaussian anticode scale

For an integer \(T\), define a graph \(\Gamma_T\) on
\(\mathcal L=\binom{[2m]}{m-1}\) by

\[
       RS\in E(\Gamma_T)\quad\Longleftrightarrow\quad
       |R\cap S|<T.                                          \tag{2.1}
\]

An independent set in \(\Gamma_T\) is exactly a \(T\)-intersecting
uniform family.

### Lemma 2.1 (uniform complete-intersection bound)

For every \(1\le T\le m-1\),

\[
 \alpha(\Gamma_T)
 \le N\exp\left(-{T^2\over2(m-1)}\right).                    \tag{2.2}
\]

#### Proof

The Complete Intersection Theorem says that a largest \(T\)-intersecting
subfamily of \(\binom{[2m]}{m-1}\) is one of

\[
 \mathcal F_i=
 \left\{R:
   |R\cap B_i|\ge T+i
 \right\},\qquad |B_i|=T+2i,                                 \tag{2.3}
\]

where \(0\le i\le m-1-T\).

For uniform \(R\), the variable \(X_i=|R\cap B_i|\) is hypergeometric
with mean

\[
 \mu_i={m-1\over2m}(T+2i).
\]

The threshold exceeds its mean by

\[
 T+i-\mu_i
 ={T\over2}+{T+2i\over2m}\ge {T\over2}.                      \tag{2.4}
\]

Hoeffding's inequality for sampling \(m-1\) points without replacement
therefore gives

\[
 {|\mathcal F_i|\over N}
 =\Pr(X_i\ge T+i)
 \le\exp\left(-{2(T/2)^2\over m-1}\right).
\]

Taking the maximum over \(i\) proves (2.2). \(\square\)

### Theorem 2.2 (endpoint matching theorem)

With \(T_\star\) as in (0.1), every
\(\mathcal U\subseteq\mathcal L\) of size \(u\) contains pairwise
vertex-disjoint pairs

\[
       (R_1,S_1),\ldots,(R_J,S_J),\qquad
       |R_j\cap S_j|<T_\star,                                \tag{2.5}
\]

where

\[
                       J\ge {u-D/2\over2}.                    \tag{2.6}
\]

#### Proof

Lemma 2.1 and the definition of \(T_\star\) give

\[
 \alpha(\Gamma_{T_\star})
 \le {N\over2m}={D\over2}.                                   \tag{2.7}
\]

Take a maximal matching in the induced graph
\(\Gamma_{T_\star}[\mathcal U]\).  Its unmatched vertices form an
independent set and hence number at most \(D/2\).  Pairing the other
vertices proves (2.6). \(\square\)

The scale in Theorem 2.2 is essentially forced for size-only reasoning:
Proposition 1.1 remains a constant-density counterexample throughout
\(T=o(\sqrt m)\).

## 3. Exact free-clone ledger

Let \(\mathcal F\) be an auxiliary matching of size

\[
                         |\mathcal F|={N-u\over2}.             \tag{3.1}
\]

Every auxiliary edge uses two owner clones.  Since there are \(W\) clones
in total, the number and density of free owner clones are exactly

\[
          W-2|\mathcal F|=W-N+u=D+u,\qquad
          f={D+u\over W}.                                    \tag{3.2}
\]

This identity has no independence or regularity hypothesis.  At the target
scale \(u\asymp D\),

\[
                         f\asymp {1\over m}.                   \tag{3.3}
\]

The two-terminal augmenter consumes exactly two of these free clones and
reduces \(u\) by two, so (3.2) remains true after every switch.

## 4. The isolated conditional moment

Take the endpoint matching from Theorem 2.2.  Put

\[
 t_j=|R_j\cap S_j|<T_\star.                                  \tag{4.1}
\]

Let \(\mathscr A_j\) be the labelled family of all oriented Theorem 2.3
augmenters with endpoints \(R_j,S_j\).  Its exact cardinality is

\[
             |\mathscr A_j|
             =(t_j+2)t_j!(t_j+1)!.                           \tag{4.2}
\]

Let \(Y_j(\mathcal F)\) count those members of \(\mathscr A_j\) for which

1. every old parity edge belongs to the projection of \(\mathcal F\); and
2. the two terminal owner pairs each have a free clone.

At \(t_j=0\) the two labels distinguish which of the two terminal
resources is called \(h\), although they encode the same direct edge.
Counting both changes all bounds by at most a factor two and matches the
exact census convention of the companion note.

Define the edge-density benchmark

\[
 \mathfrak B(\mathcal F)
 =f^2\sum_{j=1}^{J}
       {|\mathscr A_j|\over\Delta^{t_j}},
 \qquad
 \Delta=\binom{m+1}{2}.                                      \tag{4.3}
\]

No probabilistic assertion is built into this definition.

### Lemma 4.1 (the benchmark is exponentially large)

If \(u\ge D\), then

\[
             \mathfrak B(\mathcal F)
             \ge\exp\bigl((2\log2-o(1))m\bigr).               \tag{4.4}
\]

#### Proof

Theorem 2.2 gives \(J\ge D/4\), and (3.2) gives
\(f\ge1/(m+1)\).  For \(0\le t<T_\star\),

\[
 \log\left({(t+2)t!(t+1)!\over\Delta^t}\right)
 \ge-O(T_\star\log m)
 =-O\!\left(\sqrt m(\log m)^{3/2}\right)
 =-o(m).                                                      \tag{4.5}
\]

Finally

\[
 \log D=(2\log2+o(1))m.
\]

Multiplying these three lower bounds proves (4.4). \(\square\)

### Theorem 4.2 (conditional critical rounding)

Suppose that for every auxiliary matching with \(u\ge D\), one can choose
the endpoint matching in Theorem 2.2 so that

\[
 \boxed{\qquad
 \sum_{j=1}^{J}Y_j(\mathcal F)
 \ge e^{-o(m)}\,\mathfrak B(\mathcal F).
 \qquad}                                                     \tag{CM}
\]

Then there is an auxiliary matching leaving fewer than \(D\) lower
vertices uncovered.

#### Proof

By Lemma 4.1, the right side of (CM) tends to infinity.  Hence some
eligible augmenter exists.  Switch it.  The all-intersection augmenter
theorem increases the matching size by one, so \(u\) falls by two, and
it preserves every clone capacity.  Repeat while \(u\ge D\).  The process
terminates with \(u<D\). \(\square\)

The factor \(e^{-o(m)}\) in (CM) is deliberately weak.  Polynomial,
polylogarithmic, and all subexponential losses are harmless.  Thus the
unproved assertion is not a sharp concentration estimate; it merely rules
out an exponentially strong conspiracy between the old-edge events and
the two terminal free-clone events.

## 5. Component gate and compiler rate

Theorem 4.2 addresses the matching-size part of critical Kneser rounding.
The zero-signature hexagon in the companion note gives a literal
degree-preserving switch that joins three distinct quotient owner cycles.
A completely parallel remaining hypothesis is:

> whenever the \(0/2\) owner core has more than \(O(D)\) cycle
> components, at least one zero-signature hexagon has its old edges on
> three distinct cycles.

That statement is not proved here.  It is separate from (CM): the
hexagon has deterministic zero signature, so no owner-capacity correlation
remains, only its incidence with the current cycles.

For the compiler height

\[
                         H=\sqrt m\log\log m,
\]

the proved/conditional matching rate is exactly sufficient:

\[
 {D\over W/H}={H\over m+1}
 =(1+o(1)){\log\log m\over\sqrt m}\longrightarrow0.           \tag{5.1}
\]

Thus \(u=O(D)\) and \(c=O(D)\) both imply \(o(W/H)\), with no hidden
loss from the Gaussian endpoint scale \(T_\star\).  Alternating paths are
switched simultaneously; their length does not create additional omitted
owners.  This is only the \(q=1\) owner/component ledger: no assertion is
made here that a pre-existing deeper \(H\)-safe chronology survives these
switches.

## 6. Honest conclusion

The strongest unconditional result here is Theorem 2.2: every
Catalan-scale-or-larger leave contains linearly many disjoint endpoint
pairs admitting exact augmenters of length
\[
                     O(\sqrt{m\log m}).
\]
The exact free-clone density is (3.2), and the natural conditional moment
over those endpoints is exponentially large even after every
subexponential loss.

What remains unproved is only that enough of the prescribed old paths and
terminal free clones occur **together** in the current matching, plus the
separate hexagon/cycle incidence.  Proposition 1.1 shows why the more
attractive \(O(\log m)\) endpoint theorem cannot be obtained from leave
size alone.
