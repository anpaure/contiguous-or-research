# One projected MSW matching: exact run obstruction and quotient-shadow ledger

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web
input is used.

## 0. Outcome

Let

\[
 p=2m+1\ {\rm be\ prime},\qquad
 W=\binom pm,\qquad T={W\over p},
\]

and let \(B_{\rm MSW}\) be the projected \(p\)-regular bipartite graph on
the two copies of the translation-necklace set.  For one perfect matching
\(M\), let \(s(M)\) be the sum, over the oriented MSW rows, of the cyclic
run counts of the selected arc subsets.  Throughout \(H=o(p)\).

The requested estimate

\[
                         s(M)=o(T/H)                 \tag{0.1}
\]

is not proved here.  What is proved is an exact, genuinely one-matching
obstruction which is stronger than the earlier one-factorization gate.

For \(1\le L\le p\), let \(\nu_L\) be the maximum total arc weight of a
vertex-disjoint packing, on the split necklace shores, by cyclic MSW-row
intervals of length at least \(L\), with complete rows also admitted.
Then every perfect matching satisfies

\[
 \boxed{
                         s(M)\ge{T-\nu_L\over L}
                         \qquad(1\le L\le p).}       \tag{0.2}
\]

Consequently, a single estimate

\[
                         \nu_{cH}\le(1-\delta)T       \tag{0.3}
\]

for fixed \(c,\delta>0\) would refute (0.1) by giving

\[
                         s(M)\ge{\delta\over c}{T\over H}
\]

for every perfect matching.  Conversely, (0.1) forces

\[
                         \nu_L=T-o(T)                \tag{0.4}
\]

for some \(L/H\to\infty\), \(L=o(p)\).  Thus the minimal quotient gate is
an almost-spanning long-interval packing/extension theorem.  Ordinary
perfect-matching Hall does not see it.

There is an exact spectral form as well.  If \(U\) rotates every MSW row
by one arc, and \(K\) is the common zero space of the two necklace-fibre
averaging projections, define

\[
 \gamma_{\rm MSW}
 =\inf_{0\ne f\in K}{\|(I-U)f\|_2^2\over\|f\|_2^2}.             \tag{0.5}
\]

Then

\[
 \boxed{
 s(M)\ge{\gamma_{\rm MSW}\over2}
             T\left(1-{1\over p}\right).}           \tag{0.6}
\]

Hence \(\gamma_{\rm MSW}H\not\to0\) is another quantitative obstruction.
The uniform fractional point has zero seam cost, so neither regularity nor
the ordinary matching polytope can supply such a lower bound.

Finally, seam control and quotient-shadow coverage are separate.  Let
\(\mathcal R_{q}^{\pm}(M)\) be the target necklaces hit by starts whose
complete depth-\(q\) trace remains inside one selected MSW-row run, and put

\[
 K_q={1\over p}\binom p{m-q},\qquad
 \Delta_{\rm inh}(M)
 =\sum_{q=1}^H\sum_{\epsilon\in\{-,+\}}
       \bigl(K_q-|\mathcal R_q^\epsilon(M)|\bigr).              \tag{0.7}
\]

If \(\mathfrak H_{\rm quot}(M)\) is the aggregate two-sign quotient hole
count, then exactly

\[
 \boxed{
 \Delta_{\rm inh}(M)-2H^2s(M)
 \le\mathfrak H_{\rm quot}(M)
 \le\Delta_{\rm inh}(M),}                           \tag{0.8}
\]

with the lower bound truncated at zero depth by depth.

Thus (0.1) alone does not imply aggregate \(o(T)\) quotient holes: its
available error in (0.8) is only \(o(TH)\).  If the stronger
\(H^2s(M)=o(T)\) holds, then aggregate \(o(T)\) holes are equivalent to
\(\Delta_{\rm inh}(M)=o(T)\).  At one fixed depth \(q\le H\), (0.1) does
make the seam ambiguity \(o(T)\), but cross-row target collisions still
require an independent union theorem.

## 1. Exact binary run formula

Write the arcs of an oriented MSW row \(C\) as

\[
                         e_{C,0},e_{C,1},\ldots,e_{C,p-1}
\]

in cyclic order, and put

\[
 x_{C,i}=\mathbf1_{\{e_{C,i}\in M\}}.               \tag{1.1}
\]

Let

\[
                         A_C(M)=\{i:x_{C,i}=1\}.
\]

If \(A_C\) is a nonempty proper subset, let \(r_C(M)\) be its number of
cyclic interval components.  Set \(r_C=0\) for an empty or complete row.
By definition,

\[
                         s(M)=\sum_Cr_C(M).          \tag{1.2}
\]

### Lemma 1.1 (three exact seam identities)

For every perfect matching \(M\),

\[
 \boxed{
\begin{aligned}
 s(M)
 &=T-\sum_{C,i}x_{C,i}x_{C,i+1}\\
 &={1\over2}\sum_{C,i}|x_{C,i+1}-x_{C,i}|\\
 &={1\over2}\|(I-U)x\|_2^2 .
\end{aligned}}                                      \tag{1.3}
\]

Indices are cyclic in every row.

#### Proof

If a proper selected subset of one row has \(k\) positions and \(r\)
cyclic runs, it has exactly \(k-r\) adjacent selected pairs.  A complete
row has \(p\) selected positions and \(p\) adjacent selected pairs, while
an empty row contributes zero.  Summing and using
\(\sum_{C,i}x_{C,i}=|M|=T\) proves the first line.

A binary cyclic word with \(r\) one-runs has exactly \(2r\) transitions.
This proves the second line.  For binary coordinates,
\(|a-b|=(a-b)^2\), proving the third. \(\square\)

This formula uses only the selected matching.  No other \(p-1\) colour
classes are present.

## 2. Matching constraints as two exact resolutions

Let \(P_0\) average a function on tagged MSW arcs over each common left
necklace fibre, and let \(P_1\) average over each common right necklace
fibre.  Every such fibre has \(p\) tagged arcs.  The perfect-matching
equations are exactly

\[
                         P_0x=P_1x={1\over p}\mathbf1.          \tag{2.1}
\]

Put

\[
                         f=x-{1\over p}\mathbf1.
\]

Then

\[
                         f\in K:=\ker P_0\cap\ker P_1           \tag{2.2}
\]

and a direct calculation gives

\[
 \|f\|_2^2
 =T\left(1-{1\over p}\right).                    \tag{2.3}
\]

Since \(U\mathbf1=\mathbf1\), Lemma 1.1 gives

\[
                         2s(M)=\|(I-U)f\|_2^2.      \tag{2.4}
\]

Taking the infimum in (0.5) proves (0.6).

The spectral obstruction may vanish: a nonzero row-constant vector in
\(K\) has zero \(U\)-energy.  Such vectors are precisely real kernel
directions of the row--necklace incidence matrix after removing the
constant vector.  Therefore (0.6) is useful only after the actual MSW
double resolution is shown to have a quantitative gap on that kernel.
No such gap is asserted here.

There is also an exact audit of the relaxation.  The constant vector

\[
                         x_e={1\over p}              \tag{2.5}
\]

satisfies (2.1) and \(Ux=x\), so its relaxed seam cost is zero.  In the
whole-row hypergraph, the constant row weight \(1/p\) likewise covers
every necklace with mass one.  Thus a positive integral obstruction
cannot follow from \(p\)-regularity, ordinary Hall, or the unlifted
matching polytope.  It must detect the integral interval geometry in
Section 3 or an equivalent all-order cylinder.

## 3. The long-interval packing obstruction

Split every middle necklace into a left and a right vertex.  A cyclic
interval \(I\) of consecutive arcs in one MSW row occupies the left
endpoints and right endpoints of those arcs.  Call \(I\) admissible when
these \(2|I|\) endpoint occurrences define a matching in
\(B_{\rm MSW}\).  Complete transversal rows are also admitted, with
weight \(p\).

For \(L\le p\), let \(\mathcal I_{\ge L}\) be this weighted interval
hypergraph and define

\[
 \nu_L
 =\max\left\{
       \sum_{I\in\mathcal P}|I|:
       \mathcal P\text{ is a vertex-disjoint packing in }
                         \mathcal I_{\ge L}\right\}.             \tag{3.1}
\]

### Theorem 3.1 (exact interval-deficiency lower bound)

Every perfect matching \(M\) satisfies (0.2).

#### Proof

Decompose the selected positions in every partial row into their maximal
cyclic runs, and regard every complete selected row as one complete
interval.  These intervals are pairwise vertex-disjoint on both necklace
shores because they are subsets of one perfect matching.

Delete every partial run of length less than \(L\).  There are at most
\(s(M)\) deleted runs, each of length at most \(L-1\).  The retained
intervals form a packing in \(\mathcal I_{\ge L}\) of weight at least

\[
                         T-(L-1)s(M).
\]

Therefore

\[
                         \nu_L\ge T-(L-1)s(M),
\]

which implies the slightly stronger bound

\[
                         s(M)\ge{T-\nu_L\over L-1}
\]

when \(L>1\), and hence (0.2).  For \(L=1\), the assertion is trivial.
\(\square\)

### Corollary 3.2 (the exact obstruction scale)

If (0.3) holds for some fixed \(c,\delta>0\), then every perfect matching
has

\[
                         s(M)\ge
                         {\delta+o(1)\over c}{T\over H}.
                                                               \tag{3.2}
\]

Thus a positive-density weighted-packing deficit at interval scale
\(\Theta(H)\) is a literal lower obstruction to the required little-oh
bound.

The packing number has a standard fractional dual.  If nonnegative
weights \(a_v\) on the split necklace vertices satisfy

\[
                         \sum_{v\in V(I)}a_v\ge|I|
 \qquad(I\in\mathcal I_{\ge L}),                    \tag{3.3}
\]

then

\[
                         \nu_L\le\sum_va_v.          \tag{3.4}
\]

However, on a completely necklace-transversal MSW core this fractional
dual can never prove (0.3).  Restrict for the moment to intervals of one
fixed length \(L\).  Every split necklace vertex has \(p\) physical
occurrences, and each occurrence belongs to exactly \(L\) cyclic
length-\(L\) intervals.  Hence every vertex has interval degree \(pL\).
Assigning

\[
                         z_I={1\over pL}             \tag{3.5}
\]

to every length-\(L\) interval gives vertex load one and fractional
objective

\[
 (Tp)\,L\,{1\over pL}=T.                            \tag{3.6}
\]

Summing the vertex-capacity inequalities over the \(2T\) split vertices
shows that no fractional packing can have weight more than \(T\).
Therefore (3.6) is an exact fractional perfect packing, and every dual
weight satisfying (3.3) has total at least \(T\).

After deleting the polynomially many nontransversal rows supplied by the
prime-cycle transversality theorem, the same calculation loses only
\(o(T)\) mass.  Thus a positive-density deficit in (0.3), if it exists,
is necessarily an **integral** interval-packing gap.  Ordinary weighted
Hall and first-marginal cylinder counts cannot detect it.

### Corollary 3.3 (necessary long-interval packing)

If perfect matchings satisfy \(Hs(M)/T\to0\), then there is a sequence
\(L\) with

\[
                         H=o(L),\qquad L=o(p),        \tag{3.7}
\]

for which

\[
                         \nu_L=T-o(T).               \tag{3.8}
\]

#### Proof

Put \(\delta=Hs(M)/T=o(1)\).  If \(s(M)=0\), take
\(L=\lfloor\sqrt{Hp}\rfloor\).  Otherwise choose

\[
 L=H\min\{\delta^{-1/2},(p/H)^{1/2}\}
\]

with harmless rounding.  Then \(L/H\to\infty\), \(L/p\to0\), and

\[
                         Ls(M)=o(T).
\]

The retained-run packing in the proof of Theorem 3.1 has weight
\(T-o(T)\). \(\square\)

This is necessary, not sufficient.  A large interval packing need not
extend to a perfect matching of \(B_{\rm MSW}\).  If one can instead find
an extendable interval packing of length at least \(L\), weight
\(T-r\), and \(k\) partial intervals, then any perfect-matching extension
has

\[
                         s(M)\le k+r.               \tag{3.9}
\]

Indeed the prescribed intervals contribute at most \(k\) runs, and each
of the \(r\) remaining selected edges can create at most one additional
run.  Thus the concrete positive target is

\[
                         L/H\to\infty,\qquad
                         k+r=o(T/H).                 \tag{3.10}
\]

This condition produces the desired one matching directly and invokes no
low-switch colouring of the complement.

## 4. Exact inherited-window shadow sandwich

Fix one sign \(\epsilon\) and depth \(q\).  In the physical lift of
\(M\), mark the quotient seam positions at which the selected successor
does not continue along the same translated MSW row.  There are
\(s(M)\) such quotient seam orbits in the exact row-cost model.

Let \(D_{q}^{\epsilon}(M)\) be the quotient starts whose depth-\(q\)
trace crosses a marked seam.  The two parity choices differ by one
predecessor shift, and the exact predecessor-dilation identity gives

\[
                         |D_q^\epsilon(M)|
                         \le(2q-1)s(M).             \tag{4.1}
\]

For starts outside \(D_q^\epsilon(M)\), the trace is a genuine translated
MSW trace.  Let

\[
                         \mathcal R_q^\epsilon(M)
\]

be the set of target necklaces hit by these inherited starts.  Let
\(\mathcal A_q^\epsilon(M)\) be the set hit by all starts.  Then

\[
 \mathcal R_q^\epsilon(M)\subseteq
 \mathcal A_q^\epsilon(M),\qquad
 |\mathcal A_q^\epsilon(M)\setminus
        \mathcal R_q^\epsilon(M)|
                         \le|D_q^\epsilon(M)|.       \tag{4.2}
\]

Every nontrivial target translation orbit has size \(p\), so the number
of target necklaces on either sign at depth \(q\) is

\[
                         K_q={1\over p}\binom p{m-q}.            \tag{4.3}
\]

Here the lower rank is \(m-q\), while the complementary upper rank is
\(m+1+q\); the two layers have the same cardinality.

Writing

\[
 \mathfrak H_{q,\epsilon}^{\rm quot}(M)
 =K_q-|\mathcal A_q^\epsilon(M)|,                  \tag{4.4}
\]

equations (4.1)--(4.2) give the exact sandwich

\[
 \boxed{
 \left(K_q-|\mathcal R_q^\epsilon(M)|
              -(2q-1)s(M)\right)_+
 \le\mathfrak H_{q,\epsilon}^{\rm quot}(M)
 \le K_q-|\mathcal R_q^\epsilon(M)|.}              \tag{4.5}
\]

Summing (4.5) and using

\[
                         \sum_{q=1}^H(2q-1)=H^2
\]

proves (0.8).

### Consequences

1. At one fixed \(q\le H\), if \(s(M)=o(T/H)\), then the ambiguity
   between actual holes and inherited-union holes is \(o(T)\).
2. Summed through all \(H\) depths and both signs, the available ambiguity
   is \(2H^2s(M)\).  The requested seam estimate controls this only by
   \(o(TH)\), not \(o(T)\).
3. If \(H^2s(M)=o(T)\), then
   \[
    \mathfrak H_{\rm quot}(M)=o(T)
    \quad\Longleftrightarrow\quad
    \Delta_{\rm inh}(M)=o(T).                       \tag{4.6}
   \]
4. Without the stronger seam scale, aggregate \(o(T)\) holes can still
   occur, but only through direct coverage by the seam-crossing starts or
   through a sharper overlap identity.  Run count alone cannot certify
   it.

## 5. Certified boundary

Proved:

1. the three exact one-matching run identities (1.3);
2. the spectral obstruction (0.6);
3. the long-interval packing lower bound (0.2);
4. the precise positive extendable-packing criterion (3.10);
5. the exact inherited-shadow sandwich (4.5); and
6. the aggregate two-sign ledger (0.8).

Not proved:

1. an actual extendable MSW interval packing satisfying (3.10);
2. a positive-density dual weight proving (0.3);
3. a perfect matching with \(s(M)=o(T/H)\);
4. \(\Delta_{\rm inh}(M)=o(T)\) for the same matching; or
5. aggregate \(o(T)\) quotient holes.

The full \(p\)-colour low-switch theorem is unnecessary.  The remaining
structural problem is exactly one extendable long-interval packing, while
the coverage problem is the independent all-depth union functional
\(\Delta_{\rm inh}\).
