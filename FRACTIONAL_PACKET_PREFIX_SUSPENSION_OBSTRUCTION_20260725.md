# Prefix suspension defeats the first canonical rebundling

Date: 2026-07-25

Method: pure mathematics only.  No web search, finite search, random
experiment, solver, or unproved asymptotic theorem is used.

## 0. Outcome

Let

\[
 n=2m+1,\qquad t=\operatorname{Cat}_m,
\]

and let \(F_m^\dagger\) be the exact factor constructed in Section 6 of
`FRACTIONAL_PACKET_CANONICAL_MSW_OBSTRUCTION_20260725.md`: starting from the
canonical MSW factor, simultaneously switch every size-two
\((2\ 3)\)-interaction component

\[
 \mathcal C_{0,1100V},\qquad V\in\mathcal D_{m-4}.
\]

That rebundling removes the original \(\operatorname{Cat}_{m-4}\) packet
family based on the three roots

\[
 11110000,\qquad11101000,\qquad11001100.
\]

It does **not** remove the packet obstruction itself.  For every \(m\ge6\)
and every balanced quota system containing depth one,

\[
 \boxed{
  \vartheta(F_m^\dagger,\beta)
  \ge \operatorname{Cat}_{m-4}-\operatorname{Cat}_{m-6}.
 }
 \tag{0.1}
\]

Since

\[
 \frac{\operatorname{Cat}_{m-4}-\operatorname{Cat}_{m-6}}
      {\operatorname{Cat}_m}
 =\frac{15}{4096}+O(m^{-1}),
 \tag{0.2}
\]

the explicitly repaired factor still fails \((\mathrm{FSP}_A)\) by a factor
of order \(\sqrt m\).

The obstruction is again edit-robust.  If \(F\) is any exact factor and

\[
 d(F,F_m^\dagger)
 :=|F_m^\dagger\setminus F|
  =|F\setminus F_m^\dagger|,
\]

then

\[
 \boxed{
  \vartheta(F,\beta)
  \ge
  \bigl(\operatorname{Cat}_{m-4}-\operatorname{Cat}_{m-6}
               -d(F,F_m^\dagger)\bigr)_+.
 }
 \tag{0.3}
\]

Thus escaping the original canonical obstruction by the explicit
positive-density rebundling is not enough: any subsequent successful route
must make a further positive-density change away from the repaired factor.

The mechanism is a **prefix suspension**.  Prepending a Dyck word to the old
collision seed moves the collision to a later block of the MSW trajectory.
A prefix-free family consisting of \(10\) and every primitive Dyck word of
semilength at least three avoids the two removed root cylinders \(1100*\)
and \(1010*\).  Catalan convolution gives the exact count in (0.1).

## 1. Exact concatenation of MSW flip permutations

Write \(\mathcal D_s\) for the Dyck words of semilength \(s\).  If
\(P\in\mathcal D_p\) and \(Q\in\mathcal D_q\), coordinates of \(Q\) in the
concatenated word \(PQ\) are shifted by \(2p\).

### Lemma 1.1 -- concatenation law

The canonical MSW flip permutation satisfies

\[
 \boxed{
  \pi(PQ)=\pi(P)\,\Vert\,\bigl(2p+\pi(Q)\bigr).
 }
 \tag{1.1}
\]

Consequently, during the first \(p\) complete moves of the column rooted at
\(PQ\), the suffix \(Q\) is fixed and the prefix follows the complete
column rooted at \(P\).  After those \(p\) moves the state is

\[
 \overline P\,Q,
 \tag{1.2}
\]

where \(\overline P\) is the bitwise complement of \(P\).  The next \(q\)
complete moves fix \(\overline P\) and reproduce, with coordinate offset
\(2p\), the column rooted at \(Q\).

#### Proof

The permutation identity is an induction on \(p\).  The empty prefix is
immediate.  For nonempty \(P\), write its first-return decomposition as

\[
 P=1u0v,
\]

where \(u,v\) are Dyck.  Then \(PQ=1u0(vQ)\).  Apply the recursive MSW
formula

\[
 \pi(1u0v)
 =\bigl(|u|+2,\ |u|+2-\pi(\operatorname{rev}u),\ 1,\
              |u|+2+\pi(v)\bigr).
 \tag{1.3}
\]

The only term changed by appending \(Q\) is \(\pi(v)\).  Since \(v\) has
smaller semilength than \(P\), induction gives

\[
 \pi(vQ)=\pi(v)\,\Vert\,\bigl(|v|+\pi(Q)\bigr),
\]

where word lengths, rather than semilengths, are used in the offsets.  The
offset of the final block in (1.3) is therefore

\[
 |u|+2+|v|=|P|=2p.
\]

This proves (1.1).

Write

\[
 \pi(P)=(a_0,b_0,\ldots,a_{p-1},b_{p-1}).
\]

The \(i\)-th complete move changes coordinate \(a_i\) from zero to one and
coordinate \(b_i\) from one to zero.  Since \(\pi(P)\) is a permutation of
the \(2p\) prefix coordinates, after the first \(p\) moves every prefix bit
has been toggled exactly once, while (1.1) shows that no suffix coordinate
has changed.  This proves (1.2).  The last assertion follows from the
second block of (1.1).  \(\square\)

### Corollary 1.2 -- prefix-and-suffix suspension of an internal colour

Let \(w\in\mathcal D_s\), let \(x_i(w)\) be its state after \(i\) complete
moves, where \(1\le i\le s-1\), and let

\[
 \Gamma_w(x_i)=x_i\cup\{a_i,b_{i-1}\}
 \tag{1.4}
\]

be its internal second-upper colour.  For Dyck words
\(P\in\mathcal D_p\) and \(V\in\mathcal D_v\), the corresponding state in
the column rooted at \(PwV\), after \(p+i\) complete moves, is

\[
 \overline P\,x_i(w)\,V,
\]

and its colour is

\[
 \boxed{
  \Gamma_{PwV}=\overline P\,\Gamma_w(x_i)\,V.
 }
 \tag{1.5}
\]

#### Proof

Apply Lemma 1.1 twice:

\[
 \pi(PwV)
 =\pi(P)\,\Vert\,(2p+\pi(w))\,\Vert\,
   (2p+2s+\pi(V)).
\]

At time \(p+i\), the prefix has become \(\overline P\), the seed state is
\(x_i(w)\), and the suffix is still \(V\).  Both coordinates adjoined in
(1.4) lie in the seed block, so adjoining them gives (1.5).  \(\square\)

## 2. A shifted three-owner collision

Use the audited semilength-four collision seed

\[
 w^{(1)}=11110000,
 \qquad
 w^{(2)}=11101000,
 \qquad
 w^{(3)}=11001100.
 \tag{2.1}
\]

At their second internal states they have the common colour

\[
 T_0=10111101.
 \tag{2.2}
\]

Take the prefix

\[
 P=10.
\]

It has semilength one and \(\overline P=01\).  For every
\(V\in\mathcal D_{m-5}\), Corollary 1.2 gives the common colour

\[
 \boxed{
  T_V^\sharp=01\,T_0\,V
              =0110111101V
 }
 \tag{2.3}
\]

in the three canonical wreaths rooted at

\[
 10w^{(1)}V,qquad10w^{(2)}V,qquad10w^{(3)}V.
 \tag{2.4}
\]

The word in (2.3) has \(m+2\) ones.  Hence it determines the lower
depth-one target

\[
 S_V^\sharp
 =\{\infty\}\cup\bigl([2m]\setminus T_V^\sharp\bigr),
 \qquad |S_V^\sharp|=m-1.
 \tag{2.5}
\]

Distinct suffixes give distinct targets and pairwise disjoint triples of
owner wreaths.  This follows simply from the uniqueness of the root word in
the canonical MSW factor: all three ten-letter prefixes in (2.4) are fixed
and distinct, and the remaining suffix is exactly \(V\).

The same argument gives a reusable cylinder statement.

### Proposition 2.1 -- arbitrary-prefix collision cylinder

Fix any Dyck prefix \(P\in\mathcal D_p\).  Let \(F\) be an exact factor
which contains, for all but \(d\) suffixes
\(V\in\mathcal D_{m-p-4}\), all three canonical wreaths

\[
 E(Pw^{(1)}V),\qquad E(Pw^{(2)}V),\qquad E(Pw^{(3)}V).
 \tag{2.6}
\]

Then every balanced quota system containing depth one satisfies

\[
 \boxed{
  \vartheta(F,\beta)
  \ge
  \bigl(\operatorname{Cat}_{m-p-4}-d\bigr)_+.
 }
 \tag{2.7}
\]

#### Proof

For every intact suffix, (1.5) suspends the common seed colour to

\[
 \overline P\,T_0V.
\]

The three rows in (2.6) are owners of its complementary lower depth-one
target.  For quota one choose any two; for quota two choose all three.
Different intact suffixes use disjoint canonical rows.  The resulting
packets have congestion one, proving (2.7).  \(\square\)

## 3. The shifted owners survive every defining switch of \(F_m^\dagger\)

For \(V\in\mathcal D_{m-4}\), switching
\(\mathcal C_{0,1100V}\) removes exactly the two canonical rows

\[
 11001100V,\qquad10101100V,
 \tag{3.1}
\]

and replaces them by their \((2\ 3)\)-transposes.

Every root in (2.4) begins with \(1011\): the prefix is \(10\), and all
three seed roots in (2.1) begin with \(11\).  Therefore none has either
form in (3.1), whose two roots begin with \(1100\) and \(1010\),
respectively.  The three canonical owner rows in (2.4) all remain literally
present in \(F_m^\dagger\).

It is irrelevant whether the new transposed rows create additional owners
of \(S_V^\sharp\).  The three displayed surviving owners are already enough
to select the required survival packet.

## 4. A prefix-free safe code and proof of (0.1)

The single prefix \(P=10\) already gives
\(\operatorname{Cat}_{m-5}\) disjoint packets.  A larger prefix-free code
gives the stronger bound in (0.1).

Call a nonempty Dyck word **primitive** when it returns to height zero only
at its final step.  Let

\[
 \mathscr P^\dagger
 =\{10\}
 \cup
 \{P:P\text{ is primitive Dyck of semilength }p\ge3\}.
 \tag{4.1}
\]

This is a prefix-free family.  Indeed, if one primitive Dyck word were a
proper prefix of another, the longer word would return to zero before its
end.  The word \(10\) begins with \(10\), whereas every primitive word of
semilength at least two begins with \(11\).

Every prefix in \(\mathscr P^\dagger\) is safe from (3.1).  The word \(10\)
followed by any seed in (2.1) begins with \(1011\).  A primitive Dyck word
of semilength at least three begins with \(11\), cannot begin with \(1100\)
because that would return to zero after four steps, and therefore begins
with neither \(1100\) nor \(1010\).

For every \(P\in\mathscr P^\dagger\) of semilength \(p\le m-4\) and every
\(V\in\mathcal D_{m-p-4}\), the three canonical rows

\[
 E(Pw^{(1)}V),\qquad E(Pw^{(2)}V),\qquad E(Pw^{(3)}V)
 \tag{4.2}
\]

remain in \(F_m^\dagger\) and own the common target whose upper-core word is

\[
 \overline P\,T_0V.
 \tag{4.3}
\]

These targets are all distinct, including across different prefix lengths.
To see this, view a bit word as a height walk.  Since \(P\) is primitive
Dyck, \(\overline P\) stays strictly below zero until returning to zero at
its final step.  Hence the first return to zero in (4.3) uniquely recovers
the end of \(\overline P\), and therefore recovers \(P\).  Removing that
prefix and the fixed word \(T_0\) then recovers \(V\).

The owner triples in (4.2) are pairwise disjoint.  If two owner roots were
equal, the shorter of their two code prefixes would be a prefix of the
longer.  Prefix-freeness forces the prefixes to agree; then the fixed
eight-letter seed block recovers \(j\), and the remaining suffix recovers
\(V\).

At depth one every balanced quota is either one or two.  For each resource
(4.3), choose any two of its three displayed owners when its quota is one,
and choose all three when its quota is two.  These are pairwise disjoint
survival packets.

There is one code prefix of semilength one.  The number of primitive Dyck
words of semilength \(p\) is \(\operatorname{Cat}_{p-1}\).  Hence the
packet count is

\[
\begin{aligned}
 L_m
 &=
 \operatorname{Cat}_{m-5}
 +\sum_{p=3}^{m-4}
   \operatorname{Cat}_{p-1}\operatorname{Cat}_{m-p-4}\\
 &=
 \operatorname{Cat}_{m-4}-\operatorname{Cat}_{m-6}.
 \tag{4.4}
\end{aligned}
\]

For the last equality put \(N=m-5\) and use the Catalan convolution

\[
 \sum_{r=0}^{N}\operatorname{Cat}_r\operatorname{Cat}_{N-r}
 =\operatorname{Cat}_{N+1}.
\]

Indeed, the sum over \(p\ge3\) is the part with \(r=p-1\ge2\); adding the
\(\operatorname{Cat}_{N}\) term from \(P=10\) cancels the omitted \(r=0\)
term, leaving only the omitted \(r=1\) term
\(\operatorname{Cat}_{N-1}\).  Giving every selected packet weight one is
a feasible packet packing of value \(L_m\), proving (0.1).

For (0.3), at most one of these pairwise disjoint owner triples can be hit
by each removed row of \(F_m^\dagger\).  Hence at least

\[
 \bigl(L_m-d(F,F_m^\dagger)\bigr)_+
\]

triples remain literally intact in \(F\).  Select their two- or three-owner
packets according to their quotas.  They remain pairwise disjoint, proving
(0.3).  \(\square\)

## 5. General prefix-cylinder obstruction

The preceding proof is not special to the two cylinders defining
\(F_m^\dagger\).

For a nonempty Dyck word \(U\in\mathcal D_u\), write

\[
 [U]_m=\{UZ:Z\in\mathcal D_{m-u}\}
 \tag{5.1}
\]

for its canonical root cylinder in semilength \(m\).

### Theorem 5.1 -- bounded-prefix rebundlings retain Catalan packet mass

Let \(\mathscr U_m\) be any family of nonempty Dyck words of semilength at
most \(r\).  Suppose an exact factor \(F\) contains every canonical MSW row
whose root lies outside

\[
 \bigcup_{U\in\mathscr U_m}[U]_m.
 \tag{5.2}
\]

Then every balanced quota system containing depth one satisfies

\[
 \boxed{
  \vartheta(F,\beta)
  \ge
  \mathcal N_{m,r}
  :=
  \sum_{p=r+1}^{m-4}
  \operatorname{Cat}_{p-1}\operatorname{Cat}_{m-p-4}.
 }
 \tag{5.3}
\]

Equivalently,

\[
 \boxed{
  \mathcal N_{m,r}
  =
  \operatorname{Cat}_{m-4}
  -
  \sum_{a=0}^{r-1}
  \operatorname{Cat}_{a}\operatorname{Cat}_{m-5-a}.
 }
 \tag{5.4}
\]

If \(r\le(m-5)/2\), then

\[
 \boxed{
  \mathcal N_{m,r}\ge\frac12\operatorname{Cat}_{m-4}.
 }
 \tag{5.5}
\]

More generally, for every \(r\le m-5\),

\[
 \boxed{
  \mathcal N_{m,r}\ge\operatorname{Cat}_{m-5}.
 }
 \tag{5.6}
\]

Thus no rebundling whose removed canonical support is confined to proper
Dyck-prefix cylinders of maximum semilength at most \(m-5\) can satisfy
\((\mathrm{FSP}_A)\).  The half-depth hypothesis in (5.5) only improves
the asymptotic density from at least \(1/1024\) to at least \(1/512\).

#### Proof

Use every primitive Dyck prefix \(P\) of semilength

\[
 r<p\le m-4.
\]

Such a \(P\) cannot begin with a member \(U\in\mathscr U_m\).  Otherwise it
would return to height zero at the end of \(U\), strictly before its own
end, contradicting primitivity.  Therefore all three canonical rows
\(Pw^{(j)}V\) lie outside (5.2) and remain in \(F\).

Primitive Dyck words of all semilengths form a prefix-free family.  Their
complements are negative primitive excursions, so the first-return
decoding used in Section 4 shows that all suspended targets
\(\overline P T_0V\) are distinct.  Hence Proposition 2.1 gives one
pairwise disjoint packet for each pair

\[
 P\in\mathcal D_p\text{ primitive},\qquad
 V\in\mathcal D_{m-p-4}.
\]

There are \(\operatorname{Cat}_{p-1}\) primitive prefixes of semilength
\(p\), proving (5.3).  Put \(a=p-1\) and use Catalan convolution to obtain
(5.4).

For (5.5), put \(N=m-5\).  The summands

\[
 \operatorname{Cat}_{a}\operatorname{Cat}_{N-a}
\]

are symmetric under \(a\leftrightarrow N-a\).  When \(r\le N/2\), the
retained tail \(a\ge r\) contains at least one member of every symmetric
pair and contains the central term when \(N\) is even.  It therefore has
at least half of the full convolution
\(\operatorname{Cat}_{N+1}=\operatorname{Cat}_{m-4}\).

Finally, if \(r\le m-5\), the retained sum (5.3) includes its endpoint
\(p=m-4\), which equals

\[
 \operatorname{Cat}_{m-5}\operatorname{Cat}_0
 =\operatorname{Cat}_{m-5}.
\]

This proves (5.6).  \(\square\)

## 6. What this proves and what it does not

### Proved

1. MSW flip permutations concatenate exactly as in (1.1).
2. Every finite internal collision admits simultaneous Dyck-prefix and
   Dyck-suffix suspension, with the prefix complemented in the colour.
3. The all-size-two native rebundling \(F_m^\dagger\) leaves
   \(\operatorname{Cat}_{m-4}-\operatorname{Cat}_{m-6}\) pairwise disjoint
   three-owner depth-one packets.
4. Consequently
   \(\vartheta(F_m^\dagger,\beta)=\Omega(t)\) for every balanced quota
   system, and this explicit repaired factor still fails
   \((\mathrm{FSP}_A)\).
5. An \(o(t)\)-row perturbation of \(F_m^\dagger\) also fails; a further
   \((15/4096-o(1))t\) row replacement is necessary.

### Not proved

1. This does not disprove \((\mathrm{FSP}_A)\) over the whole exact-factor
   fibre.
2. It does not show that every positive-density rebundling leaves a finite
   collision seed.
3. It does not rule out a further switch family that also removes the
   prefix-code collision cylinders.  It proves that the first rebundling
   must itself be followed by another positive-density change.

The conceptual gain is that deleting one prefix-cylinder collision is not
stable under the MSW concatenation structure.  The same local seed reappears
one irreducible Dyck block later, outside the switched cylinders.

## 7. Adversarial self-audit

1. **The prefix is complemented.**  The suspended colour is
   \(01T_0V\), not \(10T_0V\), because the complete first prefix move
   toggles both bits of \(10\).
2. **The owner roots are not complemented.**  They remain the original
   roots \(10w^{(j)}V\); complementation occurs in the internal state, not
   in the root label.
3. **No hidden assumption about exact owner multiplicity is used.**  The
   argument needs only three surviving owners.  Extra owners created by the
   switches cannot invalidate a selected packet.
4. **Quota two is handled.**  When the quota is two, the entire surviving
   triple is a three-owner packet.  Thus assigning every available upper
   quota to these targets does not remove the obstruction.
5. **The switch cylinders are checked at four bits.**  The \(P=10\) roots
   begin \(1011\).  A longer primitive prefix begins \(11\) but cannot begin
   \(1100\), since that would be an internal return to zero.  Thus no code
   root begins \(1100\) or \(1010\).
6. **Owner disjointness uses prefix-freeness.**  Equal roots would force the
   shorter code prefix to prefix the longer one.  Primitive Dyck words,
   together with the separate word \(10\), form a prefix-free code.
7. **Target distinctness is a separate check.**  It is not inferred from
   owner disjointness.  The first-return decomposition of the negative
   primitive word \(\overline P\) uniquely decodes \(P\) from the target
   colour; the fixed seed then decodes \(V\).
8. **The Catalan density has two terms.**  The safe code count is
   \(\operatorname{Cat}_{m-4}-\operatorname{Cat}_{m-6}\), with limiting
   density \(4^{-4}-4^{-6}=15/4096\).
