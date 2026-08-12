# Paired-\(C_6\) completion: exact all-depth neutrality and the MWB no-go

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web
input is used.

## 0. Verdict

The fresh-hub star-to-star seam in
MATH_THEOREM_PAIRED_C6_STAR_TO_STAR_PACKET_20260726.md
is a literal local geodesic packet. It also has a literal rowwise
\(\infty\)-closing completion on three cyclic words. That completion
includes every previously omitted collar and transported-tail window.

The exact result is negative for MWB:

\[
 \boxed{\text{the completed three-row packet has zero carrier at every
 cyclic interval length.}}                            \tag{0.1}
\]

Consequently a bank of independent Catalan suspensions, even at positive
density, leaves every shallow histogram, every mobile balanced-quota
distance, and every completion-spill term exactly unchanged. It can
preserve a quota-safe core, but it cannot create one.

There is a sharp dichotomy.

1. Keep the router open in order to retain its nonidentity \(3\)-cycle:
   it is not a rooted wreath packet. A positive-density disjoint bank
   needs \(\Omega(\operatorname {Cat}_m)\) affected roots to be
   reconnected and cannot be the core of the
   \(o(\operatorname {Cat}_m/\sqrt m)\)-completion theorem.
2. Close it by the aligned literal completion below: the monodromy is
   repaired, but its complete all-depth carrier is identically zero.

Thus this packet does not prove coefficient one. A useful successor must
have a nonzero **final**, collision-summed, mobile-quota carrier; a local
incidence switch or nonidentity open monodromy is insufficient.

## 1. The completed cyclic words

Let \(m\ge5\). Partition the finite coordinate set as

\[
 [2m]
 =C\mathbin{\dot\cup}D\mathbin{\dot\cup}
   \{u,v,k,k',a_0,a_1,a_2\},                          \tag{1.1}
\]

where

\[
 |C|=m-3,\qquad |D|=m-4.                              \tag{1.2}
\]

Fix orders

\[
 \mathbf C=(c_1,\ldots,c_{m-3}),\qquad
 \mathbf D=(d_1,\ldots,d_{m-4}),                      \tag{1.3}
\]

and use petal indices modulo three. Define cyclic coordinate words

\[
\begin{aligned}
 \Phi_i={}&
 (k,u,a_i,\mathbf C,a_{i+1},v,k',
       \mathbf D,a_{i+2},\infty),\\
 \Psi_i={}&
 (k,u,a_{i+1},\mathbf C,a_i,v,k',
       \mathbf D,a_{i+2},\infty).
\end{aligned}                                         \tag{1.4}
\]

Each word contains every coordinate exactly once.

Use the notation of the paired-\(C_6\) packet:

\[
\begin{aligned}
 S_i&=C\cup\{u,k,a_i\},&
 T_i&=C\cup\{u,a_i,a_{i+1}\},\\
 A_i&=C\cup\{v,a_i,a_{i+1}\},&
 B_i&=C\cup\{v,k',a_i\},                              \tag{1.5}
\end{aligned}
\]

and

\[
\begin{aligned}
 U_i&=C\cup\{u,k,a_i,a_{i+1}\},\\
 V_i&=C\cup\{u,v,a_i,a_{i+1}\},\\
 Z_i&=C\cup\{v,k',a_i,a_{i+1}\}.                     \tag{1.6}
\end{aligned}
\]

For a cyclic word \(\Pi\), write \(I_\Pi(h,r)\) for its cyclic
length-\(r\) interval starting at \(h\).

### Theorem 1.1 (literal rowwise completion)

The first four middle windows are

\[
\begin{array}{c|cccc}
 &h=0&h=1&h=2&h=3\\ \hline
 \Phi_i&S_i&T_i&A_i&B_{i+1}\\
 \Psi_i&S_{i+1}&T_i&A_i&B_i .
\end{array}                                           \tag{1.7}
\]

Their adjacent unions are, in order,

\[
                         U_i,\qquad V_i,\qquad Z_i.    \tag{1.8}
\]

After the displayed star-to-star packet, the remaining exchanges are

\[
 c_r\longmapsto d_r\quad(1\le r\le m-4),\qquad
 c_{m-3}\longmapsto a_{i+2}.                          \tag{1.9}
\]

Finally,

\[
\begin{aligned}
 I_{\Phi_i}(m,m)
  &=D\cup\{v,k',a_{i+1},a_{i+2}\}
    =[2m]\setminus S_i,\\
 I_{\Psi_i}(m,m)
  &=D\cup\{v,k',a_i,a_{i+2}\}
    =[2m]\setminus S_{i+1}.                           \tag{1.10}
\end{aligned}
\]

Hence the \(\infty\)-cut closes every word to its own complementary
endpoint. The local twists \(\tau\) and \(\tau^{-1}\) do not survive as
global wreath monodromy.

#### Proof

The first \(m\) symbols of \(\Phi_i\) are
\((k,u,a_i,\mathbf C)\). Advancing once inserts \(a_{i+1}\) and removes
\(k\), advancing twice inserts \(v\) and removes \(u\), and advancing
three times inserts \(k'\) and removes \(a_i\). This gives the first line
of (1.7), and the three unions are (1.8).

The same calculation for \(\Psi_i\) starts at \(S_{i+1}\), inserts
\(a_i\), then \(v\), then \(k'\), giving the second line. The rest of the
two words gives (1.9). The window beginning at position \(m\) consists
of the next \(m\) finite coordinates and is exactly the corresponding
set in (1.10). Every exchange is permanent, so each rooted path is a
Johnson geodesic of length \(m\). The final Kneser edge across
\(\infty\) closes the minimum wreath. \(\square\)

### Proposition 1.2 (root-clean choice)

Suppose \(k=1\), the least finite coordinate, and the three \(S_i\) are
Dyck roots. Then each family in (1.4) is \(D_m\)-port-clean: its rooted
path contains no other Dyck state.

#### Proof

Every Dyck \(m\)-set contains coordinate \(1\). The first exchange in
both settings removes \(k=1\), which is never reinserted. Every later
lower state therefore omits \(1\) and is not Dyck. \(\square\)

This choice matters. In the superficially natural local assignment

\[
 u=1,\quad k=2,\quad (a_0,a_1,a_2)=(3,4,5),\quad v=6, \tag{1.11}
\]

the lower states of the original two-step packet are

\[
\begin{array}{c|ccc}
 &S_i&T_i&A_i\\ \hline
 i=0&123&134&346\\
 i=1&124&145&456\\
 i=2&125&135&356 .
\end{array}                                           \tag{1.12}
\]

They contain all five \(D_3\)-roots, although there are only three
paths. Hence, in the natural root-prefix (or affine order-preserving)
Catalan suspension which sends these five local roots to five distinct
\(D_m\)-roots, the exact remaining-root Hall lemma forbids extending
even one packet to a \(D_m\)-port factor. For \(t\) such contexts with
disjoint lower resources, its root deficit is exactly \(2t\). Swapping
\(u\) and \(k\) removes this particular obstruction, but not the
all-depth neutrality below.

Indeed, a prescribed family of \(t\) paths extendible to a complete
\(D_m\)-port factor can contain exactly \(t\) Dyck lower states: its
\(t\) initial ports already account for them, and every additional
internal Dyck state removes one required root from the remaining path
slots. Here \(t=3\) and the packet contains five.

## 2. Physical middle-owner distinctness

The three petal slots in either word (using zero-based positions) are

\[
                         2,\qquad m,\qquad 2m-1.       \tag{2.1}
\]

Their cyclic step distances are

\[
                         m-2,\qquad m-1,\qquad4.       \tag{2.2}
\]

### Proposition 2.1 (collision threshold)

For \(m\ge5\), the \(3(2m+1)\) middle windows of
\(\{\Phi_i:i\in\mathbb Z_3\}\) are pairwise distinct. The same is true
of \(\{\Psi_i:i\in\mathbb Z_3\}\).

At \(m=4\) both assertions fail; for example,

\[
 I_{\Phi_i}(2m-1,m)
 =\{a_{i+2},\infty,k,u\}
 =I_{\Phi_{i+2}}(2m,m).                               \tag{2.3}
\]

#### Proof

All nonpetal coordinates occupy the same labelled positions in the three
words. Suppose two length-\(m\) arcs have the same set of nonpetal
coordinates. If their starting positions differ, choose the shorter
cyclic displacement, of size at most \(m\). The two equal-length arcs
then exchange two boundary position blocks of that size. Equality of the
nonpetal sets forces both boundary blocks to contain petals only.

For \(m\ge5\), the petal positions are isolated. Hence each boundary
block would have length one, and its two petal positions would be
separated by exactly \(m\). No difference of the positions in (2.1) is
\(m\) modulo \(2m+1\). Thus the two position arcs are equal.

No length-\(m\) position arc contains zero or all three petal slots:
the three intervening nonpetal runs have lengths
\(m-3,m-2,3\), all shorter than \(m\), and no one of them can contain
the complementary arc needed to place all three petals inside an
\(m\)-arc. Thus a fixed position arc contains exactly one or two petal
slots. As \(i\) varies, the resulting singleton labels, respectively
unordered petal pairs, distinguish the three rows. This proves
distinctness. The displayed equality proves the \(m=4\) failure.
\(\square\)

Thus, for \(m\ge5\), either side of (1.4) is a literal three-wreath
partial exact factor whenever its three middle-owner sets are available.

## 3. The complete all-depth carrier

The local \(X/Y\) ledger alone sees only (1.7)--(1.8). The complete
carrier must also include:

1. the post-\(B\) exchanges (1.9);
2. every interval crossing the \(\mathbf C\)-block collars;
3. intervals through the transported \(a_{i+2}\)-tail; and
4. reverse-collar intervals crossing \(\infty\).

All four classes occur in the following exact formula.

Put

\[
 \ell=m-q,\qquad \kappa=\min\{\ell,m-2\},\qquad
 \mathbf A=(k,u),\quad\mathbf R=(v,k',\mathbf D).     \tag{3.1}
\]

Let \(P_{i,h}\) and \(Q_{i,h}\) be, respectively, the sets of the last
and first \(h\) symbols of the linear word

\[
                 (\mathbf R,a_{i+2},\infty,\mathbf A),                \tag{3.2}
\]

and let \(C^{\rm pre}_r,C^{\rm suf}_r\) be the first and last \(r\)
elements of \(\mathbf C\), with the zeroth versions empty. Write
\([E]\) for the basis vector of the set \(E\).

### Theorem 3.1 (two-collar formula and exact cancellation)

The row-paired depth-\(q\) carrier
\(\delta_{i,q}=\mu_q(\Psi_i)-\mu_q(\Phi_i)\) is

\[
\begin{aligned}
 \delta_{i,q}
={}&\sum_{j=1}^{\kappa}
 \Bigl(
 [P_{i,\ell-j}\cup C^{\rm pre}_{j-1}\cup\{a_{i+1}\}]
 -
 [P_{i,\ell-j}\cup C^{\rm pre}_{j-1}\cup\{a_i\}]
 \Bigr)\\
&+\sum_{j=1}^{\kappa}
 \Bigl(
 [C^{\rm suf}_{j-1}\cup Q_{i,\ell-j}\cup\{a_i\}]
 -
 [C^{\rm suf}_{j-1}\cup Q_{i,\ell-j}\cup\{a_{i+1}\}]
 \Bigr).
                                                               \tag{3.3}
\end{aligned}
\]

Moreover,

\[
             \boxed{\sum_{i\in\mathbb Z_3}\delta_{i,q}=0
                    \quad\text{for every }0\le q\le m-1.}            \tag{3.4}
\]

#### Proof

The two words in (1.4) differ by exchanging the petal labels in the first
two petal slots. A cyclic length-\(\ell\) interval changes exactly when
it contains one of those slots and not the other. There are
\(\kappa\) such starts at each collar. Reading the common symbols on the
two sides gives precisely the two sums in (3.3).

This includes the reverse collar: explicitly,

\[
P_{i,h}=
\begin{cases}
 \operatorname {suf}_h(k,u),&h\le2,\\
 \{\infty,k,u\},&h=3,\\
 \operatorname {suf}_{h-4}(\mathbf R)
       \cup\{a_{i+2},\infty,k,u\},&h\ge4,
\end{cases}                                           \tag{3.5}
\]

while

\[
Q_{i,h}=
\begin{cases}
 \operatorname {pre}_h(\mathbf R),&h\le m-2,\\
 D\cup\{v,k',a_{i+2}\},&h=m-1.
\end{cases}                                           \tag{3.6}
\]

If a context in (3.3) is independent of \(i\), its cyclic sum is

\[
                    \sum_i([K+a_{i+1}]-[K+a_i])=0.    \tag{3.7}
\]

If it contains \(a_{i+2}\), the positive and negative terms both
enumerate the three unordered petal pairs. They again cancel as
multisets. This proves (3.4). \(\square\)

There is a shorter equivalent proof which also covers every interval
length at once. Fix a cyclic start and length. The set of nonpetal
positions in the interval is identical in the two three-row families.
At the three petal slots, the \(\Phi_i\) use the even cyclic assignments

\[
                         (a_i,a_{i+1},a_{i+2}),
\]

and the \(\Psi_i\) use the odd assignments

\[
                         (a_{i+1},a_i,a_{i+2}).
\]

For a fixed subset of zero, one, two, or three petal positions, these
assignments give the same multiset of coordinate subsets over \(i\).
Thus

\[
\boxed{
 \sum_{i,h}[I_{\Phi_i}(h,r)]
 =\sum_{i,h}[I_{\Psi_i}(h,r)]
 \quad(0\le r\le2m+1).}                               \tag{3.8}
\]

Equation (3.8) contains all lower shadows, all upper shadows, all three
displayed \(X/Y\) collars, the transported tails, and the
\(\infty\)-crossing collar.

The two triples are nevertheless not rowwise cosmetic with fixed labels.
No \(\Psi_j\) is a rotation or reversal of a \(\Phi_i\): the neighbours
of \(u\) force \(i=j+1\), while the neighbours of \(\infty\) force
\(i=j\).

For completeness, a labelled wreath support determines its cyclic order
up to rotation and reversal. Indeed, if two coordinates have shorter
cyclic distance \(d\le m\), the number of length-\(m\) owners containing
both is \(m-d\); adjacency is therefore characterized by co-occurrence
\(m-1\), and the resulting labelled cycle determines the order up to its
two orientations. Thus no individual \(\Psi_j\) has the same middle-owner
family as any \(\Phi_i\). The packet is a genuine owner trade whose
aggregate interval histogram is neutral.

## 4. Exact test against the serial weighted-quota theorem

Let \(\mathcal M^-\) be any literal partial core containing a
root-disjoint bank of \(\Phi\)-triples, and suppose replacing them by the
corresponding \(\Psi\)-triples gives another literal partial core
\(\mathcal M^+\). Let \(\mathcal C\) be one common rooted exact
completion. By (3.8),

\[
                 \mu_q^{\mathcal M^+}
                 =\mu_q^{\mathcal M^-}
                 \qquad(0\le q\le m-1).               \tag{4.1}
\]

For every balanced quota \(b_q\),

\[
\begin{aligned}
 \operatorname {Car}_{q,b_q}(\mathcal M^+)
 &=\operatorname {Car}_{q,b_q}(\mathcal M^-),\\
 \operatorname {Spill}_{q,b_q}(\mathcal C\mid\mathcal M^+)
 &=\operatorname {Spill}_{q,b_q}(\mathcal C\mid\mathcal M^-).
                                                               \tag{4.2}
\end{aligned}
\]

Therefore the exact weighted-quota costs satisfy

\[
\boxed{
 \mathcal E_A(\mathcal M^+,\mathcal C)
 =\mathcal E_A(\mathcal M^-,\mathcal C)
 \quad\text{for every }A.}                            \tag{4.3}
\]

#### Proof

Histogram equality gives the first line of (4.2). It also gives equality
of the residual capacities
\((b_q-\mu_q^{\mathcal M^\pm})_+\), so the actual completion spill is
the same. Minimizing their common sum over \(b_q\), weighting by
\(1/c_q\), and summing gives (4.3). \(\square\)

This is stronger than a small-norm estimate. The packet has **zero**
final useful carrier. It preserves quota safety if it was already
present, but it cannot reduce even one unit of balanced overload or
completion spill.

No packetwise minimization has been used: (4.1) is an equality of the
complete physical histograms before the mobile-quota hinge is applied.

## 5. Catalan suspension and the exact obstruction

There are two meanings of “suspend the router.”

### 5.1 Independent open suspension

An uncompleted paired-\(C_6\) setting has a nonidentity \(3\)-cycle on
its three star labels. For a root-disjoint family \(\Gamma\), these
cycles have disjoint supports, so their product is the identity only
when \(\Gamma\) is empty.

A partial core in the weighted-quota theorem consists of literal rooted
global wreath rows. It cannot contain an open root-to-wrong-complement
strand. Hence all three roots of every disjoint open packet must remain
outside that core until a genuine global reconnection is supplied. Thus

\[
                         R\ge3|\Gamma|.                \tag{5.1}
\]

At positive packet density, \(|\Gamma|=\Theta(B)\), equation (5.1)
gives

\[
                         R=\Theta(B)
     \ne o(B/\sqrt m).                                \tag{5.2}
\]

The direct three-stage repair is unavailable: Theorem 6.1 of the paired
packet note proves that the output petal was just inserted, while a
second nonidentity star router on the same strands must remove it. Such
a concatenation is not a Johnson geodesic.

### 5.2 Aligned literal suspension

The words (1.4) close every row exactly. Any root-disjoint Catalan
context bank for which the \(\Phi\)-triples are available can therefore
be switched literally, and the same exact completion can be retained.
However, (4.3) says that an arbitrary number of such independent
suspensions has exactly zero MWB effect.

In particular, a positive-density bank does not approach quota safety:

\[
 \mathcal M^+\text{ is quota-safe through }H_A
 \quad\Longleftrightarrow\quad
 \mathcal M^-\text{ is quota-safe through }H_A.       \tag{5.3}
\]

Thus invoking an already quota-safe \(\mathcal M^-\) would assume the
missing theorem rather than prove it.

The existence of a positive-density, mutually resource-disjoint Catalan
atlas containing these exact \(\Phi\)-triples is itself not proved here.
That packing question is immaterial to the present no-go: even granting
the strongest possible independent atlas, its complete carrier and spill
gain are zero.

## 6. Adversarial audit and minimum surviving hypothesis

1. **Local \(X/Y\) neutrality was not extrapolated.** Formula (3.3)
   explicitly includes both \(\mathbf C\)-collars, the post-\(B\) tail,
   \(a_{i+2}\), and \(\infty\).
2. **The packet is literal only for \(m\ge5\).** At \(m=4\), same-side
   middle-owner collisions invalidate the three-row factor trade.
3. **Root cleanliness is separate.** The assignment \(u=1,k=2\)
   fails the remaining-root Hall cut by two roots per packet. Choosing
   \(k=1\) removes this defect but does not change (3.8).
4. **Open and closed packets were not mixed.** The open router retains
   monodromy but is inadmissible; the aligned closed packet is admissible
   and all-depth neutral.
5. **There are no cross-packet carrier tensors for a root-disjoint
   one-packet-per-row bank.** Histograms add over complete cyclic rows,
   and each packet's complete difference is already zero. Interacting
   packets on the same rows are a different construction.
6. **The leave bound is exact in scope.** Equation (5.1) concerns the
   open disjoint suspension. A globally closed overlapping router
   network could evade it, but would require a new literal construction.

The smallest surviving coefficient-one hypothesis is therefore:

> Construct a globally monodromy-closed, geodesic, port-clean
> multi-petal or row-dependent-exterior packet whose **complete**
> collision-summed all-depth carrier is nonzero in a favourable
> mobile-quota direction; pack it on a near-full core and prove either
> quota safety with an \(o(\operatorname {Cat}_m/\sqrt m)\)-row exact
> completion or the exact structured Car+Spill bound.

The paired \(C_6\) star-to-star packet supplies the local metric and
collar geometry, but its present literal completion cannot supply this
last hypothesis. Coefficient one remains open.
