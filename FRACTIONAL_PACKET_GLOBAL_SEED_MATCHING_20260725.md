# A global first-occurrence matching of suspended MSW packet seeds

Date: 2026-07-25

Method: pure mathematics only.  No web search, finite search, random
experiment, solver, or unproved asymptotic theorem is used.

## 0. Outcome

Let

\[
 n=2m+1,\qquad t=\operatorname{Cat}_m,
\]

and let \(F_m^{\rm MSW}\) be the canonical exact wreath factor.  Define
\(L_m\) by the generating function

\[
 \boxed{
  \sum_{m\ge0}L_mz^m
  =
  \frac{z^4C(z)}
  {1-(1+z^2)\bigl(zC(z)-z^2-2z^4\bigr)-2z^6},
 }
 \tag{0.1}
\]

where

\[
 C(z)=\sum_{m\ge0}\operatorname{Cat}_mz^m
     =\frac{1-\sqrt{1-4z}}{2z}.
\]

For every balanced quota system containing depth one,

\[
 \boxed{
  \vartheta(F_m^{\rm MSW},\beta)\ge L_m.
 }
 \tag{0.2}
\]

More generally, for every exact factor \(F\),

\[
 \boxed{
  \vartheta(F,\beta)
  \ge
  \bigl(L_m-d(F,F_m^{\rm MSW})\bigr)_+.
 }
 \tag{0.3}
\]

The exact asymptotic density is

\[
 \boxed{
  \frac{L_m}{\operatorname{Cat}_m}
  \longrightarrow
  \delta_{\rm seed}
  :=
  \frac{275}{19321}
  \approx0.014233.
 }
 \tag{0.4}
\]

Thus any factor satisfying \((\mathrm{FSP}_A)\) must replace at least

\[
 \bigl(\delta_{\rm seed}-o(1)\bigr)t
\]

canonical rows.  This is a global edit-distance barrier with no
prefix-cylinder assumption.  It improves the earlier
\(1/256\approx0.003906\) canonical barrier by a factor exceeding \(3.6\).

It also strengthens the obstruction around the explicitly rebundled factor
\(F_m^\dagger\).  Since

\[
 d(F_m^\dagger,F_m^{\rm MSW})=2\operatorname{Cat}_{m-4},
\]

one has

\[
 \boxed{
  \vartheta(F_m^\dagger,\beta)
  \ge
  \bigl(L_m-2\operatorname{Cat}_{m-4}\bigr)_+,
 }
 \tag{0.5}
\]

whose normalized limit is

\[
 \delta_{\rm seed}-\frac1{128}
 =\frac{15879}{2473088}
 \approx0.006421.
 \tag{0.6}
\]

At row distance \(e\) from \(F_m^\dagger\), subtract a further \(e\) from
the right side of (0.5).

The packet matching is indexed by the first occurrence, in the primitive
Dyck-component decomposition, of one of three interchangeable seed blocks.

This matching is close to the best possible obstruction obtainable from
these local seed triples alone.  If \(\tau_{\rm seed}(m)\) is the minimum
number of canonical rows meeting every triple

\[
 \{UAV,UBV,UDDV\},
\]

then

\[
 \boxed{
  L_m\le\tau_{\rm seed}(m)\le K_m,
  \qquad
  \frac{K_m}{t}\longrightarrow
  \kappa_{\rm seed}:=\frac{129}{8450}\approx0.015266.
 }
 \tag{0.7}
\]

Thus the exact asymptotic transversal density of the full local-seed
hypergraph lies in the narrow interval

\[
 0.014233\ldots\le
 \liminf\frac{\tau_{\rm seed}(m)}t
 \le
 \limsup\frac{\tau_{\rm seed}(m)}t
 \le0.015266\ldots.
 \tag{0.8}
\]

## 1. The seed as a local substitution of primitive components

Retain the audited semilength-four collision roots

\[
 A=11110000,\qquad
 B=11101000,\qquad
 C=11001100.
 \tag{1.1}
\]

Write

\[
 D=1100.
 \tag{1.2}
\]

The words \(A,B,D\) are primitive Dyck words, while

\[
 C=DD
 \tag{1.3}
\]

is the concatenation of two copies of \(D\).  The three roots in (1.1)
own a common depth-one target through their common internal colour

\[
 T_0=10111101.
 \tag{1.4}
\]

Every Dyck word has a unique factorization into primitive Dyck components,
obtained by cutting at its successive returns to height zero.  In that
component word, call an occurrence **active** if it is

* one component equal to \(A\);
* one component equal to \(B\); or
* two consecutive components \(D,D\).

The three alternatives all have semilength four.

## 2. Clean prefixes and disjoint triples

Call a Dyck word \(U\) **clean** when its primitive-component sequence

1. contains no component \(A\) or \(B\);
2. contains no consecutive pair \(D,D\); and
3. does not end in \(D\).

The empty word is clean.

For every clean \(U\) and every Dyck suffix \(V\), form the three canonical
roots

\[
 UAV,\qquad UBV,\qquad UDDV.
 \tag{2.1}
\]

By the exact MSW concatenation law

\[
 \pi(PQ)=\pi(P)\Vert\bigl(2|P|_{\rm semi}+\pi(Q)\bigr),
 \tag{2.2}
\]

the prefix \(U\) completes before the seed block begins.  At the audited
collision state the three columns in (2.1) therefore have common colour

\[
 \overline U\,T_0V.
 \tag{2.3}
\]

Hence their three canonical wreaths own one common lower depth-one target.

### Lemma 2.1 -- first-occurrence decoding

The owner triples (2.1), over all clean \(U\) and all \(V\), are pairwise
disjoint.

#### Proof

Scan the primitive-component sequence of any root in (2.1) from the
beginning.  The clean prefix contains no active occurrence.  Since it does
not end in \(D\), no \(D,D\) occurrence crosses the boundary between \(U\)
and the inserted block.  Thus the first active occurrence is exactly

\[
 A,\qquad B,\qquad\text{or}\qquad DD,
\]

according to which member of (2.1) is present.  The prefix before that first
occurrence recovers \(U\), the occurrence recovers the chosen variant, and
the remaining component word recovers \(V\).  Therefore a canonical root
belongs to at most one displayed triple.  \(\square\)

The lower targets in (2.3) need not be proved distinct.  The packet-packing
dual has a separate variable for every packet subset.  Even if two
resources happened to coincide, the selected packet subsets below are
different and disjoint because their owner triples are disjoint.

### Lemma 2.2 -- recursive use of dirty first occurrences

The clean first-occurrence matching can be iterated inside all roots it
leaves unused.

More precisely, after removing the roots used in Lemma 2.1, every remaining
root which has an active occurrence begins uniquely with one of the dirty
prefixes

\[
 UDA,\qquad UDB,
 \tag{2.4}
\]

where \(U\) is clean, followed by an arbitrary Dyck suffix.  The family of
dirty prefixes (2.4) is prefix-free.  Inside the suffix following each such
prefix, one may independently repeat the entire construction.  Iterating
this rule produces a pairwise disjoint family of owner triples.

#### Proof

Scan to the first active occurrence.  If it is \(DD\), or if it is \(A\)
or \(B\) preceded by a component other than \(D\), the root is one of the
three members used in Lemma 2.1.  The only remaining possibility is that
the first active occurrence is \(A\) or \(B\) preceded by one \(D\).
Everything before that final \(D\) is a clean word \(U\), giving (2.4).

No dirty prefix can prefix another: its final \(A\) or \(B\) is already an
active occurrence, whereas the portion preceding the final marker in a
different dirty prefix is marker-free.  Roots in different dirty cylinders
are therefore disjoint, and all are disjoint from the clean-stage roots.

Within a fixed dirty cylinder, the suffix is an arbitrary Dyck word and the
MSW concatenation law applies unchanged.  Hence the clean-stage construction
may be repeated there.  Induction on the remaining semilength proves
pairwise disjointness at every recursion depth.  \(\square\)

## 3. Packet packing and recursive ledger

At depth one every balanced quota is one or two.  For each owner triple
in the recursive family of Lemma 2.2, select

* any two of its rows when the common target has quota one;
* all three rows when it has quota two.

Every recursively generated triple is obtained by prefixing a clean-stage
triple by a Dyck word.  Prefix suspension therefore gives a common target,
so the displayed choice is a genuine survival packet.  Lemmas 2.1--2.2
make all selected packets pairwise disjoint.  Giving each packet dual weight
one is feasible.

Let \(M_0(z)\) count the first clean stage.  It is the number of pairs
\((U,V)\) with \(U\) clean and

\[
 |U|_{\rm semi}+4+|V|_{\rm semi}=m.
 \tag{3.1}
\]

Thus

\[
 M_0(z)=z^4U_0(z)C(z).
 \tag{3.2}
\]

The dirty prefixes (2.4) have generating function

\[
 2z^6U_0(z).
 \tag{3.3}
\]

If \(M(z)=\sum_mL_mz^m\) counts the full recursive matching, Lemma 2.2
therefore gives

\[
 M(z)=M_0(z)+2z^6U_0(z)M(z).
 \tag{3.4}
\]

It remains to compute \(U_0\) and solve this identity.

## 4. Exact generating function

Let

\[
 P(z)=zC(z)
\]

be the generating function for primitive Dyck components.  The component
\(D\) contributes \(z^2\), and the two components \(A,B\) contribute
\(2z^4\).  Thus the generating function for all other primitive components
is

\[
 E(z)=P(z)-z^2-2z^4.
 \tag{4.1}
\]

Let \(U_0(z)\) count clean component sequences ending in an \(E\)-component,
together with the empty sequence, and let \(U_1(z)\) count clean sequences
ending in \(D\).  Appending a \(D\) is allowed only after a sequence counted
by \(U_0\), while an \(E\)-component may follow either state.  Hence

\[
 U_1=z^2U_0,
 \qquad
 U_0=1+E(U_0+U_1).
 \tag{4.2}
\]

Solving,

\[
 \boxed{
  U_0(z)
  =
  \frac1{1-(1+z^2)\bigl(zC(z)-z^2-2z^4\bigr)}.
 }
 \tag{4.3}
\]

Combining (3.4) with (4.3), the number \(L_m\) of recursively disjoint
triples has generating function

\[
 \begin{aligned}
 M(z)
 &=
 \frac{z^4U_0(z)C(z)}{1-2z^6U_0(z)}\\
 &=
 \frac{z^4C(z)}
 {1-(1+z^2)\bigl(zC(z)-z^2-2z^4\bigr)-2z^6},
 \end{aligned}
\]

which proves (0.1) and hence (0.2).

## 5. Singular coefficient ratio

Put

\[
 s=\sqrt{1-4z}.
\]

Then

\[
 C(z)=\frac2{1+s}=2-2s+O(s^2),
 \qquad
 zC(z)=\frac{1-s}{2}.
 \tag{5.1}
\]

At \(z=1/4\),

\[
\begin{aligned}
 E(z)
 &=\frac{55}{128}-\frac12s+O(s^2),\\
 1-(1+z^2)E(z)-2z^6
 &=d_*+\frac{17}{32}s+O(s^2),
 \qquad
 d_*=\frac{139}{256}.
 \tag{5.2}
\end{aligned}
\]

The denominator is nonzero at \(1/4\).  Moreover its subtracted term has
nonnegative coefficients and value \(117/256<1\) there, so it has no zero
of modulus below \(1/4\).  Thus the full matching kernel is

\[
 \frac1{1-(1+z^2)E(z)-2z^6}
 =
 d_*^{-1}-\frac{17}{32}d_*^{-2}s+O(s^2).
 \tag{5.3}
\]

Multiplying by \(C(z)\), the ratio of the coefficients of \(s\) in
the matching kernel times \(C\), and in \(C\), is

\[
 d_*^{-1}+\frac{17}{32}d_*^{-2}.
 \tag{5.4}
\]

The standard square-root coefficient estimate

\[
 [z^k]\sqrt{1-4z}
 \sim-\frac{4^k}{2\sqrt\pi\,k^{3/2}}
 \tag{5.5}
\]

therefore gives

\[
\begin{aligned}
 \frac{L_m}{\operatorname{Cat}_m}
 &\longrightarrow
 \frac1{4^4}
 \left(d_*^{-1}+\frac{17}{32}d_*^{-2}\right)\\
 &=
 \frac{275}{19321}.
 \tag{5.6}
\end{aligned}
\]

This proves (0.4).

## 6. Global edit robustness

The \(L_m\) owner triples are pairwise disjoint canonical row sets.  If an
exact factor \(F\) removes \(d\) canonical rows, at most \(d\) triples are
hit.  Every intact triple still supplies a two- or three-owner packet,
regardless of any new rows added to \(F\).  Thus at least
\((L_m-d)_+\) disjoint packets remain, proving (0.3).

For \(F_m^\dagger\), exactly
\(2\operatorname{Cat}_{m-4}\) canonical rows were removed.  Substituting
this into (0.3) proves (0.5).  At further row distance \(e\) from
\(F_m^\dagger\), at most another \(e\) of the still-intact global triples
can be hit.

Finally,

\[
 \delta_{\rm seed}-\frac1{128}
 =
 \frac{275}{19321}-\frac1{128}
 =
 \frac{15879}{2473088}.
 \tag{6.1}
\]

This proves (0.6).

## 7. A near-matching global transversal

The clean-prefix matching is within a small constant gap of an explicit
transversal of the entire local-seed hypergraph.

For a Dyck root \(R\), let \(a(R)\) be the number of primitive components
of \(R\) equal to \(A\).  Delete every canonical row for which \(a(R)\) is
odd.  This hits every seed triple.  Indeed, if

\[
 k=a(U)+a(V),
\]

then the three roots

\[
 UAV,\qquad UBV,\qquad UDDV
\]

have \(A\)-counts

\[
 k+1,\qquad k,\qquad k.
\]

If \(k\) is even, the first root is deleted; if \(k\) is odd, the other two
are deleted.

Let \(C_-(z)\) be the signed Dyck series in which a root receives weight
\((-1)^{a(R)}\).  Changing the sign of the single primitive component \(A\)
changes the primitive series \(P=zC\) to \(P-2z^4\).  Since a Dyck word is
a sequence of primitive components,

\[
 C_-(z)
 =\frac1{1-P(z)+2z^4}
 =\frac{C(z)}{1+2z^4C(z)}.
 \tag{7.1}
\]

Therefore the number \(K_m\) of odd-\(A\) roots is given by

\[
 \boxed{
  \sum_{m\ge0}K_mz^m
  =
  \frac12
  \left(
   C(z)-\frac{C(z)}{1+2z^4C(z)}
  \right).
 }
 \tag{7.2}
\]

At the Catalan singularity, the ratio of the square-root coefficient of
\(C/(1+2z^4C)\) to that of \(C\) is

\[
 \left(1+2\cdot4^{-4}\cdot2\right)^{-2}
 =\left(\frac{64}{65}\right)^2.
 \tag{7.3}
\]

It follows that

\[
 \frac{K_m}{\operatorname{Cat}_m}
 \longrightarrow
 \frac12\left(1-\left(\frac{64}{65}\right)^2\right)
 =\frac{129}{8450}.
 \tag{7.4}
\]

The lower bound \(\tau_{\rm seed}(m)\ge L_m\) is supplied by the disjoint
matching of Sections 2--4; the odd-\(A\) deletion set supplies the upper
bound.  This proves (0.7)--(0.8).

This transversal is a statement about which canonical rows would have to
be removed to kill this packet certificate.  It does not assert that those
rows admit replacement by an exact wreath factor.

## 8. Boundary

The theorem proves a global positive-density edit barrier around the
canonical factor and around the explicit first rebundling.  It does not
prove that every exact factor contains a suspended MSW seed, nor does it
disprove \((\mathrm{FSP}_A)\) on the full exact-factor fibre.  A candidate
factor may still move farther than \(\delta_{\rm seed}t\) from the canonical
factor and destroy this entire matching.

The exact new requirement is nevertheless stronger than before: any
successful construction must replace at least \(1.42\%\) of all canonical
wreaths in a way that cuts across the global renewal structure, not merely
through bounded-prefix cylinders.

## 9. Adversarial self-audit

1. **The marker \(DD\) must not cross the prefix boundary.**  This is why a
   clean \(U\) is required not to end in \(D\).
2. **The three variants have equal semilength.**  \(A,B\) have semilength
   four, and \(DD\) has \(2+2=4\).
3. **The target resources need not be distinct.**  The dual packing uses
   distinct disjoint packet subsets.  No invalid duplicate packet variable
   is introduced.
4. **The ordinary-component series is nonnegative.**  Removing the unique
   \(D\) at semilength two and the two words \(A,B\) at semilength four from
   the primitive series leaves the remaining primitive components.
5. **The singular denominator stays away from zero.**  At \(z=1/4\) its
   positive subtracted series is \(117/256<1\); coefficient domination
   rules out a smaller-modulus zero.
6. **The edit count is row count.**  Exact factors have the same number of
   rows, so \(d(F,F_m^{\rm MSW})\) is both the number removed and the number
   added.
7. **No claim beyond the canonical neighbourhood is made.**  The result is
   an edit barrier, not a universal obstruction to \((\mathrm{FSP}_A)\).
8. **The transversal is not an exact-factor construction.**  Deleting all
   odd-\(A\) rows hits every local seed triple, but no compatible set of new
   wreaths is supplied.
