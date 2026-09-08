# The half-exponent tensorizes over unboundedly many paired corridors

Date: 2026-07-27

Method: pure mathematics only.  No computation, finite search, solver,
probabilistic black box, or web input is used.

## 0. Outcome

Put

\[
 n=2m,\qquad R=2r+1,\qquad h=m-2r,
\tag{0.1}
\]

and work in the Gaussian annulus

\[
                         h=m^{1/2+o(1)}.
\tag{0.2}
\]

The known two-segment construction modifies one interval \(I\) of the
domino cycle and its translate \(I+r\).  Its two remote defect fronts
are separated by only \(h\), giving list exponent \(1/2-o(1)\).

This note proves that the obstruction is not confined to a bounded
number of such pairs.

### Theorem A (unbounded paired-corridor obstruction)

There are functions

\[
                         p=p(m)\longrightarrow\infty,
 \qquad
                         \ell=\ell(m),
\tag{0.3}
\]

and \(p\) mutually separated interval pairs

\[
                         I_a,\ I_a+r,
 \qquad 1\le a\le p,
\tag{0.4}
\]

such that independently repartitioning the labels inside all \(2p\)
segments gives at least

\[
 \frac1{2m}
 \left(\frac{(2\ell)!}{2^\ell}\right)^{2p}
\tag{0.5}
\]

distinct simple domino-twin packets, every one at defect at most

\[
                         s
 =8p\ell+4ph+O(p)=o(m).
\tag{0.6}
\]

Moreover

\[
 \frac{\log |\mathcal F|}
      {s\log n}
 =\frac12-o(1).
\tag{0.7}
\]

One explicit choice is

\[
 \ell=\left\lfloor m e^{-\sqrt{\log m}}\right\rfloor,
 \qquad
 p=\left\lfloor e^{\frac12\sqrt{\log m}}\right\rfloor.
\tag{0.8}
\]

Thus no stability theorem can say that every near-half configuration
is supported on \(O(1)\) paired corridors.

### Theorem B (geometric failure of bounded-corridor cover)

The intervals in Theorem A can be placed so that any cover of their
modified positions by a fixed number \(B\) of interval pairs

\[
                         K_b,\ K_b+r,
 \qquad 1\le b\le B,
\tag{0.9}
\]

has total base-interval length \(\Omega(m)\).  Hence the \(p\) active
corridors cannot be merged into boundedly many \(o(m)\)-span corridors.
The obstruction is genuinely multi-cluster, not a presentation of one
or two long corridors with artificial cuts.

### Theorem C (the correct stability scale inside the corridor model)

For a disjoint paired-corridor ensemble with lengths
\(\ell_1,\ldots,\ell_p\), put

\[
                         L=\sum_{a=1}^p\ell_a.
\tag{0.10}
\]

Its entropy and certified defect are

\[
 {\cal E}
 =4\sum_{a=1}^p\ell_a\log\ell_a+O(L),
\tag{0.11}
\]

\[
 {\cal S}
 =8L+4ph+O(p).
\tag{0.12}
\]

If \(L=o(m)\) and

\[
                         {\cal E}
 \ge\left(\frac12-o(1)\right){\cal S}\log m,
\tag{0.13}
\]

then

\[
                         ph=o(L),
\tag{0.14}
\]

and

\[
 \sum_{a=1}^p
 \ell_a\log\frac m{\ell_a}
 =o(L\log m).
\tag{0.15}
\]

Consequently, after discarding corridors of total length \(o(L)\), all
remaining corridors have length \(m^{1-o(1)}\), and their number is

\[
                         m^{o(1)}.
\tag{0.16}
\]

Their endpoints and pairing phases can therefore be recorded in

\[
                         \exp(o(m))
\tag{0.17}
\]

ways.

The corrected structural target is thus **subpolynomially many long
paired corridors**, not boundedly many.  Theorem C is a genuine
stability theorem for the explicit segment-repartition model.  It does
not prove that every near-half packet in the full catalogue has this
form.  A full classification must still reduce arbitrary packets to
this model or find an even broader source of half-exponent entropy.

## 1. Domino cells and one paired corridor

Fix a simple packet \(F\) with cyclic unordered domino word

\[
                         B_0,B_1,\ldots,B_{m-1}.
\tag{1.1}
\]

Its \(i\)-th star core and four-target cell are

\[
 A_i=B_i\cup B_{i+1}\cup\cdots\cup B_{i+r-1},
\tag{1.2}
\]

\[
 {\cal S}_i(F)
 =\{A_i\cup\{x\}:x\in B_{i-1}\cup B_{i+r}\}.
\tag{1.3}
\]

Let

\[
                         I=[t,t+\ell-1],
 \qquad
                         J=I+r
\tag{1.4}
\]

be disjoint cyclic position intervals, with

\[
                         h<\ell,\qquad \ell+h<r.
\tag{1.5}
\]

Independently repartition the \(2\ell\) labels originally in \(I\) and
the \(2\ell\) labels originally in \(J\) into ordered lists of
\(\ell\) unordered dominoes.

Write

\[
                         L_I=[t+1,t+\ell-1].
\tag{1.6}
\]

For \(I\), a core can change only at starts

\[
                         L_I\cup(L_I-r).
\tag{1.7}
\]

For \(J=I+r\), the corresponding starts are

\[
                         (L_I+r)\cup L_I.
\tag{1.8}
\]

Therefore the possible bad-core starts are exactly contained in

\[
                         L_I\cup(L_I-r)\cup(L_I+r).
\tag{1.9}
\]

The middle band is disjoint from the two remote bands.  Since

\[
                         2r=m-h,
\tag{1.10}
\]

the two remote bands differ by a cyclic shift of \(h\).  Hence

\[
 \left|
 L_I\cup(L_I-r)\cup(L_I+r)
 \right|
 =2(\ell-1)+h.
\tag{1.11}
\]

There are at most four further cells whose core is unchanged but whose
boundary dominoes meet \(I\cup J\).  Thus one paired corridor has at
most

\[
                         b(\ell)
 =2(\ell-1)+h+4
\tag{1.12}
\]

possibly changed cells.  Since the cells of \(F\) are disjoint and
each has four targets, every repartition has defect at most

\[
                         4b(\ell)
 =8\ell+4h+O(1).
\tag{1.13}
\]

This is an upper bound on defect, which is exactly what is needed for a
list-size obstruction.  Accidental additional common targets only make
the obstruction stronger.

## 2. Packing many independent corridor pairs

We first record a placement lemma.

### Lemma 2.1 (separated paired intervals)

Suppose

\[
                         p\ell=o(m),
 \qquad
                         h=o(\ell).
\tag{2.1}
\]

There are intervals \(I_1,\ldots,I_p\), each of length \(\ell\), such
that

1. all \(2p\) intervals \(I_a,I_a+r\) are disjoint;
2. the bad-core bands and boundary-only exceptional cells belonging to
   different \(a\)'s are disjoint; and
3. the base intervals \(I_a\) may be chosen approximately equally
   spaced through an arc of length \(m/4\).

#### Proof

Put

\[
                         g=\left\lfloor\frac{m}{4p}\right\rfloor
\tag{2.2}
\]

and choose base starts \(t_a=ag\) inside an arc of length \(m/4\).
Condition \(p\ell=o(m)\) gives

\[
                         \frac g\ell\longrightarrow\infty.
\tag{2.3}
\]

Since \(h=o(\ell)\), also \(g\gg\ell+h\).  Thus the base intervals,
their middle bad bands, and their \(h\)-enlarged remote bands are
pairwise disjoint.

The translate by \(r=(m-h)/2\) moves the base arc into the opposite
half of the cycle.  Because the base arc has length \(m/4\) and
\(\ell+h=o(g)\), it is disjoint from every base interval and base bad
band.  Translation preserves the gaps between different \(a\)'s, so
the translated bands are disjoint across \(a\).  For the same \(a\),
the two remote bands are allowed to overlap by \(h\); that is precisely
the overlap counted in (1.11).  The finitely many boundary-only cells
fit inside the same \(O(1)\)-enlargements. \(\square\)

For each \(a\), independently repartition the labels in \(I_a\) and
\(I_a+r\).  One segment has

\[
                         N_\ell=\frac{(2\ell)!}{2^\ell}
\tag{2.4}
\]

ordered pairings.  Thus there are \(N_\ell^{2p}\) labelled cyclic
domino words.

A simple packet support recovers its unordered domino partition and
its cyclic domino order up to the global dihedral group.  Consequently
at most \(2m\) displayed words give the same support, and

\[
                         |\mathcal F|
 \ge\frac1{2m}
 \left(\frac{(2\ell)!}{2^\ell}\right)^{2p}.
\tag{2.5}
\]

By Lemma 2.1, the possibly changed cell sets add without overlap.
Equation (1.13) gives

\[
                         |F\setminus G|
 \le p(8\ell+4h+O(1))
 =:s
\tag{2.6}
\]

for every \(G\in\mathcal F\).

Stirling's formula gives

\[
 \log|\mathcal F|
 =4p\ell\log\ell+O(p\ell+\log m).
\tag{2.7}
\]

Combining (2.6)--(2.7),

\[
 \frac{\log|\mathcal F|}{s\log n}
 \ge
 \frac12
 \frac{\log\ell-\log n}{2\log n}
 O\left(\frac h\ell+\frac1{\log m}\right).
\tag{2.8}
\]

More transparently,

\[
 \frac{\log|\mathcal F|}{s\log n}
 =
 \frac12
o(1)
\quad\text{whenever}\quad
 \frac{\log\ell}{\log m}\to1,\quad \frac h\ell\to0.
\tag{2.9}
\]

The sign of the explicit error term in (2.8) is nonpositive; (2.8) is
only being used to assert convergence to \(1/2\).

For (0.8),

\[
 p\ell
 =m e^{-\frac12\sqrt{\log m}}(1+o(1))
 =o(m),
\tag{2.10}
\]

\[
 \frac h\ell
 =m^{-1/2+o(1)}e^{\sqrt{\log m}}
 =o(1),
\tag{2.11}
\]

and

\[
 \frac{\log\ell}{\log m}
 =1-\frac1{\sqrt{\log m}}+o(1).
\tag{2.12}
\]

Also \(p\to\infty\).  This proves Theorem A.

## 3. No bounded \(o(m)\)-span corridor cover

Use the equally spaced placement in Lemma 2.1.  Ignore the harmless
length-\(\ell\) thickness and regard the base interval starts as
\(p\) points with gap \(g\).

### Lemma 3.1 (interval-cover lower bound)

If \(B<p\) intervals cover all \(p\) base intervals, then their total
length is at least

\[
                         (p-B)g+B\ell.
\tag{3.1}
\]

#### Proof

Order the \(p\) base intervals along the arc.  One covering interval
which contains \(k\) consecutive base intervals has length at least

\[
                         (k-1)g+\ell.
\tag{3.2}
\]

Splitting a cover into its \(B\) connected pieces and summing (3.2)
gives

\[
 \sum_{b=1}^B(k_b-1)g+B\ell
 =(p-B)g+B\ell.
\]

If a covering interval contains nonconsecutive selected intervals, it
also contains every selected interval between them, so no other case
occurs. \(\square\)

For fixed \(B\), equations (2.2), (2.3), and (3.1) give

\[
                         (p-B)g+B\ell
 =\left(\frac14-o(1)\right)m.
\tag{3.3}
\]

The same is true in the translated arc.  Thus any fixed number of
paired covering corridors has linear total span.  It cannot be an
\(o(m)\)-span description of the active set.  This proves Theorem B.

## 4. Restricted stability at the half exponent

We now allow unequal lengths.  Assume the paired corridors and their
bad bands are disjoint as in Lemma 2.1, and assume

\[
                         h<\min_a\ell_a,
 \qquad
                         L=\sum_a\ell_a=o(m).
\tag{4.1}
\]

Independently repartition both members of every corridor pair.  The
same count as before gives

\[
 {\cal E}:=\log|\mathcal F|
 =4\sum_a\ell_a\log\ell_a+O(L+\log m),
\tag{4.2}
\]

and the certified defect is

\[
 {\cal S}
 =8L+4ph+O(p).
\tag{4.3}
\]

Suppose

\[
 {\cal E}
 \ge\left(\frac12-\eta_m\right){\cal S}\log m,
 \qquad
                         \eta_m\to0.
\tag{4.4}
\]

Put

\[
                         D=
 \sum_a\ell_a\log\frac m{\ell_a}.
\tag{4.5}
\]

Then

\[
 \sum_a\ell_a\log\ell_a=L\log m-D.
\tag{4.6}
\]

Insert (4.2)--(4.3) and (4.6) into (4.4).  Since \(p\le L\) and
\(\log m\to\infty\), the lower-order terms are \(o(L\log m)\).  We
obtain

\[
 4L\log m-4D+o(L\log m)
 \ge
 (4-8\eta_m)L\log m
 +(2-4\eta_m)ph\log m
 +o(L\log m).
\tag{4.7}
\]

Both \(D\) and \(ph\) are nonnegative.  Therefore

\[
                         D=o(L\log m),
\tag{4.8}
\]

\[
                         ph=o(L).
\tag{4.9}
\]

This proves (0.14)--(0.15).

For a fixed \(\varepsilon>0\), let

\[
 L_{\le1-\varepsilon}
 =\sum_{\ell_a\le m^{1-\varepsilon}}\ell_a.
\tag{4.10}
\]

Every term in this sum contributes at least
\(\varepsilon\ell_a\log m\) to \(D\).  Hence

\[
                         L_{\le1-\varepsilon}
 \le\frac{D}{\varepsilon\log m}
 =o(L).
\tag{4.11}
\]

By a diagonal choice there is \(\varepsilon_m\downarrow0\) such that,
after deleting corridors of total length \(o(L)\), every remaining
length satisfies

\[
                         \ell_a\ge m^{1-\varepsilon_m}.
\tag{4.12}
\]

Since \(L<m\), the number of remaining corridors is at most

\[
                         \frac{L}{m^{1-\varepsilon_m}}
 \le m^{\varepsilon_m}
 =m^{o(1)}.
\tag{4.13}
\]

Finally, specifying the endpoints, orientations, and finite phases of
\(m^{o(1)}\) corridors costs at most

\[
 m^{O(m^{o(1)})}
 =\exp(o(m)).
\tag{4.14}
\]

This proves Theorem C.

## 5. Exact implication boundary

### Proved

1. The half-exponent construction tensorizes over
   \(p\to\infty\) separated pairs \(I_a,I_a+r\).
2. Its defect fronts add across \(a\), while the two remote fronts
   inside each pair overlap up to the \(h\)-fringe.
3. The resulting list family still has exponent \(1/2-o(1)\) with
   total defect \(o(m)\).
4. No fixed number of \(o(m)\)-span paired corridors covers the active
   positions.
5. Within the disjoint paired-corridor model, near-half entropy forces
   all but \(o(L)\) of the modified mass into \(m^{1-o(1)}\)-long
   corridors, with only \(m^{o(1)}\) surviving components.
6. Those components have only \(\exp(o(m))\) geometric metadata.

### Not proved

1. Every near-half packet in the full simple catalogue is a
   segment-repartition packet.
2. Arbitrary bad-front sets with overlaps are reducible to disjoint
   paired corridors.
3. Quotienting a corridor cluster preserves the owner/link degrees
   required by the stopped matching process.
4. The dynamic trajectory prevents several corridor clusters from
   surviving simultaneously.

The bounded-corridor stability target is therefore false.  The exact
next static target is a **paired-front decomposition theorem** with
\(m^{o(1)}\), rather than \(O(1)\), long components and
\(\exp(o(m))\) quotient complexity.
