# Owner codegrees for truncated carrier-rotor walks

## 0. Outcome

Let \(U\in\binom{[2m]}M\), where \(M=m+H\), and let the radius be \(Q\).
Write
\[
a=m-Q,\qquad b=H-Q,qquad D=ab,
\]
and let \(\Omega_Q(U)\) be the carrier-state space from
`TRUNCATED_CARRIER_ROTOR_PATH_REDUCTION_20260725.md`.

For a stationary directed walk with \(\ell\) state endpoints, the exact
one-time and two-time owner degrees can be computed.  The central identity
is
\[
\boxed{
 \frac{\deg((t,X),(t+d,Y))}{\deg(t,X)}
 =\frac{\pi_d(\delta)}{\binom m\delta^2},
 \qquad \delta=d_J(X,Y),
}
\tag{0.1}
\]
after summing over every carrier containing the prescribed owners.  Here
\(\pi_d(\delta)\) is the probability that the two owners are at Johnson
distance \(\delta\) after \(d\) rotor steps.

For \(1\le d\le Q\), the owner trajectory is deterministically geodesic:
\[
\pi_d(\delta)=\mathbf 1_{\{\delta=d\}}.
\tag{0.2}
\]
Thus the first \(Q\) two-owner codegrees are completely explicit.

For the proposed full length \(\ell=M\), repeated owners occur in only an
\(e^{-\Omega(Q)}\) fraction of stationary walks, so occurrence degrees may
be converted into ordinary support degrees at negligible loss.  A second
coupon-collector bound shows that the apparent long-lag loss in (4.3) does
not occur at Johnson distance one.  The actual maximum normalized
owner-pair codegree is \(O(m^{-2})\).  Since the edge size is
\(\Theta(m)\), this gives the borderline parameter
\(r^2\Delta_2/D_0=O(1)\).  It is substantially better than the
projective-plane scale, but it still does not fall under an audited
growing-uniformity matching theorem.

There is a useful refinement.  Split every carrier into independently
initialized chunks of length \(\ell\), where
\[
Q\ll\ell\ll m.
\tag{0.3}
\]
The reset cost is still \(o(W)\), almost every stationary chunk has distinct
owners, and the associated simple hypergraph is nearly regular with
\[
\frac{\Delta_2}{D_0}=O(m^{-2}),
\qquad
r^2\frac{\Delta_2}{D_0}=O(\ell^2/m^2)=o(1),
\tag{0.4}
\]
where \(r=\ell+1\).  This escapes the numerical projective-plane barrier,
but a growing-uniformity matching theorem using more than pair codegrees is
still required.  It is not an immediate consequence of an elementary
one-shot random-greedy estimate.

The full nested-flag extension in Sections 9--14 changes the conclusion in
one essential way.  For tagged rows of ranks \(r<s\), \(h=s-r\), a resident
chunk has exactly

\[
 c_h(\ell)=(h+1)\ell-\binom{h+1}{2}
\]

path-forced nested slot pairs.  A fixed nested target pair consequently has
the exact forced relative codegree

\[
 {c_h(\ell)\over\ell\binom sr}
\]

relative to its rank-\(s\) vertex.  Adjacent rows therefore retain
\((2+o(1))/m\) relative codegree for every \(\ell\).  Since a full flag
chunk has rank \(1+(2Q+1)\ell\), no reset-compatible choice
\(Q/\ell=o(1)\) can satisfy even
\[
 R_\ell\Delta_2/D_0=o(1);
\]
it would contradict \(Q^2/m\to\infty\).

A ladder-aware custom theorem is still numerically possible.  The concrete
choice

\[
 \boxed{\ell=\lfloor m^{3/5}\rfloor}
\]

has \(o(W)\) reset cost, \(o(W)\) aggregate scalar flag holes, and vanishing
owner/same-row nonnested interaction.  What remains open is a custom
left-saturating nibble which treats the forced nested ladders internally and
leaves only \(o(W)\) uncovered mandatory high-row targets.

## 1. Exact path counts in one carrier

Put
\[
B=\binom Mm=\binom MH,
\qquad
F=|\Omega_Q(U)|=\frac{M!}{a!b!}.
\]
Every state has indegree and outdegree \(D\).  Therefore the number of
directed walks with \(\ell\) state endpoints is
\[
P_\ell=F D^{\ell-1}.
\tag{1.1}
\]

For a fixed owner \(X\in\binom Um\), its state fibre has size
\[
G=\frac FB=(m)_Q(H)_Q.
\tag{1.2}
\]
Regularity implies that at every fixed time \(t\), exactly
\[
\boxed{\frac{P_\ell}{B}}
\tag{1.3}
\]
walks have owner \(X\).

For \(0\le t<t+d<\ell\), let
\[
p_d^U(X,Y)=\Pr(X_{t+d}=Y\mid X_t=X),
\tag{1.4}
\]
where the state at time \(t\), conditioned on owner \(X\), is uniform in
the owner fibre and subsequent rotor choices are uniform.  The number of
walks satisfying both owner conditions is exactly
\[
\boxed{
 \frac{P_\ell}{B}\,p_d^U(X,Y).
}
\tag{1.5}
\]
The formula is independent of \(t\), since every state has the same number
of prefixes and suffixes.

## 2. Radial form of the projected kernel

The carrier rotor and uniform state measure are equivariant under every
permutation of \(U\).  The stabilizer of \(X\) is transitive on the owner
sphere
\[
\mathcal S_\delta(X)=
 \{Y\in\tbinom Um:d_J(X,Y)=\delta\},
\]
whose size is
\[
s_\delta=\binom m\delta\binom H\delta.
\tag{2.1}
\]
Consequently there are numbers \(\pi_d(\delta)\ge0\), summing to one over
\(\delta\), such that
\[
\boxed{
p_d^U(X,Y)=
 \frac{\pi_d(\delta)}{\binom m\delta\binom H\delta}.
}
\tag{2.2}
\]
In particular,
\[
p_d^U(X,Y)\le
 \frac1{\binom m\delta\binom H\delta}.
\tag{2.3}
\]

Although the state chain need not be reversible, (2.2) is symmetric in
\(X,Y\): an element of \(S_U\) interchanges any ordered pair of equal-sized
sets having Johnson distance \(\delta\).

### Lemma 2.1 -- the first \(Q\) steps are geodesic

For every rotor trajectory and every \(1\le d\le Q\),
\[
\boxed{d_J(X_t,X_{t+d})=d.}
\tag{2.4}
\]
Hence (0.2) holds.

### Proof

During the first \(d\) steps, the elements leaving the owner are the
distinct queue entries
\[
z_Q,z_{Q-1},\ldots,z_{Q-d+1}.
\]
The entering elements are the successive \(y\)'s chosen from the tail.
They are distinct and lie outside the initial owner: once chosen, such an
element cannot return to the tail within \(Q\) steps.  None of the entering
elements can leave the owner within these \(d\le Q\) steps.  The endpoint
therefore deletes exactly \(d\) old elements and inserts exactly \(d\) new
ones. \(\square\)

It follows from (1.5) and (2.4) that, inside one carrier,
\[
\#\{\text{walks}:X_t=X,\ X_{t+d}=Y\}
=
\begin{cases}
\displaystyle
\frac{P_\ell}
 {B\binom md\binom Hd},&d_J(X,Y)=d\le Q,\\[3mm]
0,&d_J(X,Y)\ne d,\ d\le Q.
\end{cases}
\tag{2.5}
\]

## 3. Summing over carriers

A fixed middle owner belongs to
\[
\kappa_0=\binom mH
\tag{3.1}
\]
carriers.  If \(d_J(X,Y)=\delta\), the number of carriers containing both is
\[
\kappa_\delta=\binom{m-\delta}{H-\delta}
\qquad(0\le\delta\le H),
\tag{3.2}
\]
and zero for \(\delta>H\).  The useful cancellation is
\[
\frac{\kappa_\delta}{\kappa_0}
=\frac{\binom H\delta}{\binom m\delta}.
\tag{3.3}
\]

Thus the global degree of the time-labelled owner condition \((t,X)\) is
\[
d_1=\kappa_0\frac{P_\ell}{B},
\tag{3.4}
\]
while the codegree of \((t,X)\) and \((t+d,Y)\) is
\[
d_2=\kappa_\delta\frac{P_\ell}{B}
 \frac{\pi_d(\delta)}{\binom m\delta\binom H\delta}.
\tag{3.5}
\]
Dividing and using (3.3) proves the exact identity (0.1):
\[
\boxed{
\frac{d_2}{d_1}
=\frac{\pi_d(\delta)}{\binom m\delta^2}.
}
\tag{3.6}
\]

In particular, for \(d\le Q\), the only nonzero distance is \(\delta=d\),
and its normalized codegree is exactly
\[
\boxed{\binom md^{-2}.}
\tag{3.7}
\]

The carrier--owner codegree is also exact: for a fixed carrier \(U\), time
\(t\), and \(X\subset U\), it is \(P_\ell/B\), a \(1/B\) fraction of the
carrier degree \(P_\ell\).

## 4. Untimed pair-occurrence codegrees

Let a walk contribute one incidence for every owner occurrence.  For
distinct global owners \(X,Y\) at distance \(\delta\), the number of
owner-occurrence pairs contributed by all walks is
\[
\boxed{
C^{\rm occ}_\ell(X,Y)
=
\frac{2\kappa_\delta P_\ell}
 {B\binom m\delta\binom H\delta}
\sum_{d=1}^{\ell-1}(\ell-d)\pi_d(\delta).
}
\tag{4.1}
\]
The one-owner occurrence degree is
\[
D^{\rm occ}_\ell(X)=
\ell\kappa_0\frac{P_\ell}{B}.
\tag{4.2}
\]
Therefore
\[
\boxed{
\frac{C^{\rm occ}_\ell(X,Y)}{D^{\rm occ}_\ell(X)}
=
\frac{2}{\ell\binom m\delta^2}
\sum_{d=1}^{\ell-1}(\ell-d)\pi_d(\delta)
\le
\frac{\ell-1}{\binom m\delta^2}.
}
\tag{4.3}
\]
The crude worst distinct-owner value is consequently at most
\[
\frac{\ell-1}{m^2}.
\tag{4.4}
\]

For the original proposal \(\ell=M\), this crude bound is
\((1+o(1))/m\).  The local lag-one contribution is approximately
\(2/m^2\).  Section 5 proves that later lags cannot concentrate at distance
one, improving the true maximum to \(O(m^{-2})\).

## 5. Self-collisions are exponentially rare

The multiplicity calculation becomes an ordinary simple-hypergraph degree
calculation once owner repetitions are discarded.  In fact this costs a
negligible fraction even at the original length \(\ell=M\).

### Lemma 5.1

For \(d>Q\),
\[
\boxed{
\Pr(X_d=X_0)
\le
\exp(Qd/a)\binom{2Q}{Q}^{-1}.
}
\tag{5.1}
\]
Consequently, uniformly for \(\ell\le M\), a stationary \(\ell\)-walk has
a repeated owner with probability at most
\[
\boxed{
\epsilon_{\rm rep}
\le
M^2\exp(QM/a)\binom{2Q}{Q}^{-1}
=e^{-\Omega(Q)}.
}
\tag{5.2}
\]

### Proof

The first \(Q\) arriving elements \(y_0,\ldots,y_{Q-1}\) are distinct and
lie outside \(X_0\).  If \(X_d=X_0\), every one of them must have left the
owner by time \(d\).  A necessary condition is that each was selected as an
\(x\)-element at some transition.

Make this necessary event as easy as possible by placing all \(Q\)
distinguished arrivals in \(L\) at time zero.  Until one is selected it
stays in \(L\), and when \(k\) distinguished elements remain, the next
\(x\)-choice selects one of them with probability exactly \(k/a\).  Hence
the time \(T_Q\) needed to select all of them is the sum of independent
geometric variables
\[
T_Q=G_Q+G_{Q-1}+\cdots+G_1,
\qquad G_k\sim\operatorname{Geom}(k/a).
\]
Staggering their actual arrival times can only increase the completion
time.  For \(\theta=Q/a\), Markov's inequality gives
\[
\Pr(T_Q\le d)
\le e^{\theta d}\prod_{k=1}^Q\mathbb E e^{-\theta G_k}.
\]
For \(p=k/a\),
\[
\mathbb E e^{-\theta G_k}
=\frac{p}{p+e^\theta-1}
\le\frac{k}{k+Q}.
\]
Therefore
\[
\Pr(T_Q\le d)
\le e^{Qd/a}\prod_{k=1}^Q\frac{k}{k+Q}
=e^{Qd/a}\binom{2Q}{Q}^{-1},
\]
which proves (5.1).

Now
\[
\frac Ma=\frac{m+H}{m-Q}=1+o(1),
\]
whereas
\[
\log\binom{2Q}{Q}=Q\log4+O(\log Q).
\]
Since \(\log4-1>0\), the right side of (5.1) is
\(e^{-\Omega(Q)}\), uniformly for \(d\le M\).  There are fewer than
\(M^2\) time pairs, and returns within \(Q\) steps are impossible by Lemma
2.1.  This proves (5.2). \(\square\)

### Lemma 5.2 -- late returns to distance one

Uniformly for \(Q<d\le M\),
\[
\boxed{\pi_d(1)=e^{-\Omega(Q)}.}
\tag{5.3}
\]

### Proof

If \(d_J(X_0,X_d)=1\), then at most one of the first \(Q\) arrivals can
remain in \(X_d\), since all of them lie outside \(X_0\).  Hence at least
\(Q-1\) of those arrivals must have been selected as \(x\)-elements.

For any prescribed collection of \(k=Q-1\) arrivals, repeat the geometric
holding-time argument from Lemma 5.1 with \(k\) in place of \(Q\) and
\(\theta=k/a\).  It gives
\[
\Pr(\text{all prescribed }k\text{ arrivals are selected by }d)
\le
e^{kd/a}\binom{2k}{k}^{-1}=e^{-\Omega(Q)},
\]
uniformly for \(d\le M\).  There are only \(Q\) choices for the possibly
unselected arrival, and this polynomial factor is absorbed by the
exponential bound. \(\square\)

Combining Lemma 5.2 with (4.3), for \(\delta=1\) one has
\[
\sum_{d=1}^{\ell-1}(\ell-d)\pi_d(1)
=\ell-1+O(\ell^2e^{-cQ}),
\]
because \(\pi_1(1)=1\), \(\pi_d(1)=0\) for \(2\le d\le Q\), and (5.3)
handles every later lag.  Thus
\[
\frac{C^{\rm occ}_\ell(X,Y)}{D^{\rm occ}_\ell(X)}
\le \frac{2+o(1)}{m^2}
\qquad(d_J(X,Y)=1).
\tag{5.4}
\]
For \(2\le\delta\le H=o(m)\), the binomial coefficients are increasing in
this range, so the crude estimate (4.3) gives, uniformly for
\(\ell\le M=O(m)\),
\[
\frac{C^{\rm occ}_\ell(X,Y)}{D^{\rm occ}_\ell(X)}
\le
\frac{M}{\binom m2^2}=O(m^{-3}).
\tag{5.5}
\]
Therefore the maximum normalized distinct-owner codegree is
\[
\boxed{\frac{\Delta_2}{D_0}=O(m^{-2})}
\tag{5.6}
\]
for every \(\ell\le M\), both in the occurrence system and, after removing
the \(e^{-\Omega(Q)}\) exceptional walks, in the simple support hypergraph.

The collection of repetition-free walks is invariant under \(S_U\).
Therefore, at each fixed time, it retains the same fraction
\(1-\epsilon_{\rm rep}\) in every owner fibre.  All one-owner degrees after
this restriction are still exact up to the common factor
\(1-\epsilon_{\rm rep}\).

Thus all full length-\(M\) one- and two-owner occurrence estimates above
also hold for the ordinary support hypergraph after multiplication by
\(1+o(1)\).

## 6. What the length-\(M\) codegrees do and do not give

After discarding the exponentially rare self-colliding walks, an owner-only
length-\(M\) atom has rank \(r\asymp m\), and (5.6) gives
\[
\Delta_2/D_0=O(1/m^2),
\qquad
r^2\Delta_2/D_0=O(1).
\tag{6.1}
\]
This escapes the elementary projective-plane counterexample, whose relative
codegree is \(1/r\), not \(1/r^2\).  It is nevertheless a borderline rather
than a vanishing interaction parameter.  The fixed-uniformity near-matching
theorems cannot be substituted diagonally at \(r\to\infty\), while the
audited genuinely growing-uniformity economical-cover bounds deteriorate
exponentially in \(r\).  Thus the calculation does not by itself prove an
owner-near-transversal.  It does show that the full stationary-path system
is materially more favorable than the earlier crude \(O(1/m)\) audit
suggested.

Independent path choice also remains unusable: the mean owner load is
\(1-o(1)\), so it leaves a positive fraction of owners uncovered.

## 7. A reset-compatible short-chunk refinement

Choose \(\ell\) such that
\[
Q\ll\ell\ll m;
\tag{7.1}
\]
this is possible because
\[
Q=(1+o(1))\sqrt{m(\log\log m+\gamma)}
\]
is \(o(m)\).  Let
\[
K=\lfloor M/\ell\rfloor.
\]
For each carrier introduce \(K\) labelled copies, and choose one independently
initialized repetition-free \(\ell\)-walk for each copy.

The literal reset cost is
\[
O(QK N_H)=O((Q/\ell)W)=o(W).
\tag{7.2}
\]
The omitted remainder contains fewer than \(\ell N_H=O((\ell/m)W)=o(W)\)
owner slots.  Thus this modification preserves the \(W+o(W)\) ledger.

Form a hypergraph with

* one vertex for every labelled carrier copy;
* one vertex for every global middle owner;
* one edge consisting of a carrier-copy vertex and the \(\ell\) distinct
  owners of one simple chunk.

Let
\[
D_L=(1-\epsilon_{\rm rep})P_\ell.
\]
Every left vertex has degree \(D_L\).  Every owner has degree
\[
D_R=
K\binom mH\frac{\ell(1-\epsilon_{\rm rep})P_\ell}{B}
=\rho_\ell D_L,
\tag{7.3}
\]
where the incidence identity
\[
N_H B=W\binom mH
\]
gives
\[
\rho_\ell=\frac{K\ell N_H}{W}
=1-O((H+\ell)/m)=1-o(1).
\tag{7.4}
\]
Thus the hypergraph is asymptotically regular.

Two left vertices have codegree zero.  A left vertex and an owner have
normalized codegree at most
\[
O(\ell/B).
\]
By (5.6), two distinct owners have normalized codegree at most
\[
\boxed{
\frac{\Delta_2}{\min(D_L,D_R)}
\le O(m^{-2}).
}
\tag{7.5}
\]
Since the rank is \(r=\ell+1\),
\[
r^2\frac{\Delta_2}{D_0}
=O(\ell^2/m^2)=o(1).
\tag{7.6}
\]

This is a genuine improvement over the full length-\(M\) atom.  It does not
by itself finish the proof: the audited fixed-uniformity matching theorems
cannot be applied diagonally, and pair-codegrees alone are not a complete
growing-rank criterion.  What remains is now the following more favorable,
object-specific statement.

> **Chunked carrier-path near-factor gate.** For some
> \(Q\ll\ell\ll m\), the simple carrier-path hypergraph above has a
> matching covering all but \(o(W)\) owner vertices and all but
> \(o(W/\ell)\) carrier-copy vertices.

Such a matching would supply the middle-owner near-transversal with
negligible reset cost.  The same calculation must then be extended to the
two flag families through depth \(Q\); their nested same-endpoint
codegrees, rather than the owner codegrees computed here, are the likely
next bottleneck.

## 8. Calibrated conclusion

The exact owner codegrees reveal two different regimes.

1. **One full \(M\)-walk per carrier.** Self-collisions are exponentially
   rare, so the support hypergraph is asymptotically regular.  Its normalized
   pair-codegree is \(O(1/m^2)\) at rank \(\Theta(m)\), putting
   \(r^2\Delta_2/D_0\) at the constant boundary.  This is promising but is
   not an application of an audited growing-rank theorem.
2. **Many sublinear chunks per carrier.** If
   \(Q\ll\ell\ll m\), resets remain negligible, self-collisions are
   negligible, degrees are asymptotically equal, and the normalized pair
   codegree is \(O(1/m^2)\), so \(r^2\Delta_2/D_0=o(1)\).  This is a
   substantially cleaner matching
   gate, but still needs a path-specific growing-uniformity nibble or an
   equivalent constructive argument.

Thus the requested owner-near-transversal does not currently follow from an
elementary matching estimate for the original length-\(M\) atoms.  The
codegree computation nevertheless produces a strict new reduction whose
matching parameters are materially better.

## 9. Extension to the full tagged flag hypergraph

The owner-only hypergraph omits the decisive nested correlations.  We now
include them exactly.

Let the signed row-tag set be

\[
 \mathcal R_Q=
 \{(-,q):1\le q\le Q\}\cup\{0\}
 \cup\{(+,q):1\le q\le Q\}.
\tag{9.1}
\]

For a tag \(\alpha\), put

\[
 r_\alpha=
 \begin{cases}
 m-q,&\alpha=(-,q),\\
 m,&\alpha=0,\\
 m+q,&\alpha=(+,q).
 \end{cases}
\tag{9.2}
\]

At a state \(\omega_t\), write \(F_\alpha(\omega_t)\) for the corresponding
target \(L_q(\omega_t)\), \(X(\omega_t)\), or \(U_q(\omega_t)\).
Targets in two different signed rows are treated as different tagged
vertices even if their underlying masks happen to agree.

Choose a chunk length \(\ell\), put

\[
 J=\left\lfloor{M\over\ell}\right\rfloor,\qquad
 S_\ell=J\ell N_H,
\tag{9.3}
\]

and make \(J\) labelled copies of every carrier.  A full flag edge consists
of one carrier-copy vertex and the \(\ell\) target occurrences in every one
of the \(2Q+1\) tagged rows.

For the moment this is an occurrence multihypergraph.  Section 12 below
gives the capacity-one/mandatory-target augmentation and removes the
low-row self-collisions.

### Theorem 9.1 -- exact one-row degrees

Let \(A\in\binom{[2m]}{r_\alpha}\).  Its occurrence degree in tagged row
\(\alpha\) is

\[
 \boxed{
 D_\alpha(A)
 =J\binom{2m-r_\alpha}{M-r_\alpha}
   {\ell P_\ell\over\binom M{r_\alpha}}
 ={J\ell N_H P_\ell\over\binom{2m}{r_\alpha}}.}
\tag{9.4}
\]

Consequently, relative to the carrier-copy degree \(P_\ell\), its symmetric
load is

\[
 \boxed{
 \mu_\alpha
 ={D_\alpha(A)\over P_\ell}
 ={S_\ell\over\binom{2m}{r_\alpha}}.}
\tag{9.5}
\]

### Proof

There are \(\binom{2m-r_\alpha}{M-r_\alpha}\) carriers containing \(A\).
At every fixed time, a uniform state in such a carrier has the prescribed
rank-\(r_\alpha\) flag with probability
\(\binom M{r_\alpha}^{-1}\).  There are \(\ell\) time positions and \(J\)
copies of every carrier.  This gives the first expression in (9.4).
Double-counting pairs \((A,U)\) gives the second. \(\square\)

Thus the full physical-row hypergraph is not nearly regular: at distance
\(q\),

\[
 \mu_q^\pm={S_\ell\over N_q},
\tag{9.6}
\]

which grows from \(1-o(1)\) at the middle to
\((1-o(1))\lambda_Q=\log m\,e^{\gamma+o(1)}\) at the outer controlled
rows.  High rows must use mandatory target vertices and surplus waste slots
rather than one capacity-one resource for every occurrence.

## 10. Exact nested-row codegrees

Fix two distinct row tags \(\alpha,\beta\), with

\[
 r=r_\alpha<s=r_\beta,\qquad h=s-r.
\tag{10.1}
\]

### Theorem 10.1 -- one time-pair

At one prescribed pair of time slots, a nested target pair \(A\subset B\),
\(|A|=r,|B|=s\), has exact conditional ratios

\[
 \boxed{
 {\deg_t(A,B)\over\deg_t(B)}
 ={1\over\binom sr},\qquad
 {\deg_t(A,B)\over\deg_t(A)}
 ={1\over\binom{2m-r}{h}}.}
\tag{10.2}
\]

Here \(\deg_t\) denotes the global occurrence count at a fixed compatible
time-pair for which the two path flags are always nested.

### Proof

For such a slot pair every chunk supplies one nested pair.  The global
coordinate action is transitive on pairs \(A\subset B\) of the prescribed
ranks.  Conditional on \(B\), its rank-\(r\) member is therefore uniform
over the \(\binom sr\) subsets of \(B\).  Conditional on \(A\), the larger
member is uniform over the \(\binom{2m-r}{h}\) rank-\(s\) supersets.
\(\square\)

The compatible time offsets can be counted without any probability.
Represent the lower flag \(L_q(\omega_t)\) by its forward owner interval
\([t,t+q]\), and the upper flag \(U_q(\omega_t)\) by its backward owner
interval \([t-q,t]\).  The path-hitting identities imply the following.

- For two lower rows, the smaller target's owner interval contains the
  larger target's interval.
- For two upper rows, the larger target's owner interval contains the
  smaller target's interval.
- For a lower and an upper row, the smaller target is contained in the
  larger whenever the two owner intervals intersect.

In all three cases, after orienting \(t\) as the time of the smaller-rank
slot and \(u\) as the time of the larger-rank slot, the compatible offsets
are exactly

\[
 u-t=0,1,\ldots,h.
\tag{10.3}
\]

Since \(h\le2Q<\ell\), their number in an \(\ell\)-chunk is

\[
 \boxed{
 c_h(\ell)
 =\sum_{d=0}^h(\ell-d)
 =(h+1)\ell-\binom{h+1}{2}.}
\tag{10.4}
\]

### Theorem 10.2 -- exact path-forced contribution

For \(A\subset B\) as above, the path-forced part of their untimed
occurrence codegree is

\[
 \boxed{
 C_{\alpha\beta}^{\rm forc}(A,B)
 ={J N_H P_\ell\,c_h(\ell)
   \over
   \binom{2m}{s}\binom sr}.}
\tag{10.5}
\]

Its exact normalized ratios are

\[
 \boxed{
 {C_{\alpha\beta}^{\rm forc}(A,B)\over D_\beta(B)}
 ={c_h(\ell)\over\ell\binom sr},}
\tag{10.6}
\]

\[
 \boxed{
 {C_{\alpha\beta}^{\rm forc}(A,B)\over D_\alpha(A)}
 ={c_h(\ell)\over\ell\binom{2m-r}{h}}.}
\tag{10.7}
\]

### Proof

There are \(J N_H P_\ell\) indexed chunks before a carrier copy is chosen.
Every compatible slot pair supplies one nested pair, and transitivity
distributes these occurrences uniformly over the
\(\binom{2m}{s}\binom sr\) nested pairs.  This proves (10.5).
Divide by (9.4) and use

\[
 \binom{2m}{s}\binom sr
 =\binom{2m}{r}\binom{2m-r}{h}
\]

to obtain (10.6)--(10.7). \(\square\)

For adjacent rows, \(h=1\) and \(c_1(\ell)=2\ell-1\).  Uniformly throughout
the controlled band,

\[
 \boxed{
 \max\left\{
 {C_{\alpha\beta}^{\rm forc}\over D_\alpha},
 {C_{\alpha\beta}^{\rm forc}\over D_\beta}
 \right\}
 ={2+o(1)\over m}.}
\tag{10.8}
\]

For fixed \(h\ge2\), the forced ratio is

\[
 O\!\left({h+1\over\binom{m-O(Q)}h}\right).
\tag{10.9}
\]

Thus the first-order obstruction is exactly the adjacent nested ladder, not
a same-rank owner collision.

## 11. Upper codegrees for arbitrary tagged rows

The preceding contribution is exact but need not be the entire codegree:
at incompatible time offsets, two path flags may become nested or acquire
another intersection type accidentally.  There is a uniform orbit upper
bound which requires no mixing assertion.

Let \(A\) have rank \(r\), let \(B\) have rank \(s\), and put

\[
 j=|A\cap B|.
\tag{11.1}
\]

The stabilizer of \(B\) is transitive on the rank-\(r\) sets with
intersection \(j\), and that orbit has size

\[
 \mathcal O_{r,s,j}
 =\binom sj\binom{2m-s}{r-j}.
\tag{11.2}
\]

### Theorem 11.1 -- arbitrary tagged-row upper bound

For any two tagged rows, any two physical targets \(A,B\), and any two
distinct time slots,

\[
 \boxed{
 {\deg_{t,u}(A,B)\over\deg_u(B)}
 \le {1\over\mathcal O_{r,s,j}}.}
\tag{11.3}
\]

After summing all ordered time pairs in an \(\ell\)-chunk,

\[
 \boxed{
 {C_{\alpha\beta}^{\rm occ}(A,B)\over D_\beta(B)}
 \le {\ell\over\mathcal O_{r,s,j}}.}
\tag{11.4}
\]

The reverse normalized ratio is obtained by interchanging
\((r,A)\) and \((s,B)\).

### Proof

Condition on the event that the second tagged slot equals \(B\).  Global
coordinate equivariance makes every member of the orbit (11.2) equiprobable
at the first slot.  The total conditional probability assigned to that
orbit is at most one, proving (11.3).  There are at most \(\ell^2\) ordered
time pairs, whereas (9.4) contains the factor \(\ell\), proving (11.4).
\(\square\)

Several useful specializations follow.

1. If \(A\subset B\) and \(h=s-r\), then
   \[
    {C_{\alpha\beta}^{\rm occ}(A,B)\over D_\beta(B)}
    \le {\ell\over\binom sh}.
   \tag{11.5}
   \]
2. For two distinct targets in one rank at Johnson distance \(\delta\),
   \[
    {C_{\alpha\alpha}^{\rm occ}(A,B)\over D_\alpha(B)}
    \le
    {\ell\over
      \binom{r_\alpha}{\delta}
      \binom{2m-r_\alpha}{\delta}}.
   \tag{11.6}
   \]
   In particular the crude same-row value at distance one is
   \(O(\ell/m^2)\).  At the owner row, Sections 4--5 improve this to
   \(O(m^{-2})\), uniformly for \(\ell\le M\).
3. The smallest nontrivial orbit in two different near-middle ranks is the
   adjacent nested orbit, of size \(m+O(Q)\).  Therefore
   \[
      {\Delta_2^{\rm flag}\over D_0}
      \le O(\ell/m)
   \tag{11.7}
   \]
   at the purely orbit-counting level, while (10.8) gives the unavoidable
   lower bound \((2+o(1))/m\).

Equations (10.5)--(10.9) and (11.3)--(11.7) are the requested
exact/upper codegree table for arbitrary tagged rows.

### Proposition 11.2 -- carrier-copy pairs

Let \(\xi=(U,j)\) be one labelled carrier copy.

1. Two distinct carrier-copy vertices have codegree zero.
2. If \(A\in\binom{[2m]}{r_\alpha}\), then
   \[
    \deg(\xi,(\alpha,A))
    =
    \begin{cases}
    \displaystyle{\ell P_\ell\over\binom M{r_\alpha}},
       &A\subset U,\\[2mm]
    0,&A\not\subset U.
    \end{cases}
   \tag{11.8}
   \]
3. Consequently
   \[
    {\deg(\xi,(\alpha,A))\over\deg(\xi)}
    ={\ell\over\binom M{r_\alpha}},
   \tag{11.9}
   \]
   and, when \(A\subset U\),
   \[
    {\deg(\xi,(\alpha,A))\over D_\alpha(A)}
    ={1\over
      J\binom{2m-r_\alpha}{M-r_\alpha}}.
   \tag{11.10}
   \]

These identities follow directly from the uniform one-time flag marginal.
They also remain valid with \(P_\ell^{\rm rs}\) after the row-simple
restriction in Section 12.

## 12. Support simplification and balanced row augmentation

The ordinary hypergraph must not count the same low-load target twice in
one edge.  This is negligible precisely on the rows where capacity one is
needed.

Put

\[
 c_\ell={W\over S_\ell}.
\tag{12.1}
\]

Since \(0\le M-J\ell<\ell\), the crossing calibration gives

\[
 W-S_\ell=O\!\left({W(H+\ell)\over m}\right).
\tag{12.2}
\]

If \(N_q\ge S_\ell\), then \(\lambda_q\le c_\ell\).  From
\(\log\lambda_q\ge q^2/(m+q)\) and
\(\log c_\ell=O((H+\ell)/m)\), every low-load row has

\[
 q\le q_\ell:=O(\sqrt{H+\ell}).
\tag{12.3}
\]

For the chunk scale chosen in Section 14, \(q_\ell=o(Q)\).

### Lemma 12.1 -- low-row repetitions are negligible

Assume

\[
 Q\ll\ell=o(m),\qquad q_\ell=o(Q).
\tag{12.4}
\]

The fraction of stationary \(\ell\)-chunks which repeat a target in any
low-load tagged row is \(e^{-\Omega(Q)}\).

### Proof

If the same lower or upper depth-\(q\) target occurs at two times, the two
middle owners are at Johnson distance at most \(q\).  For two times whose
separation is at most \(Q\), the resident geodesic property and
\(2q_\ell<Q\) show more: the first new arrival belongs to the later flag
but not the earlier one, so equality is impossible.

At a larger separation, distance at most \(q_\ell\) forces at least
\(Q-q_\ell=(1-o(1))Q\) of the first \(Q\) new arrivals to have left the
owner.  Apply the geometric coupon bound of Lemma 5.1 with
\(Q-q_\ell\) distinguished arrivals.  Since \(\ell=o(m)\), its positive
exponential term is \(o(Q)\), while the central-binomial denominator is
\(e^{(\log4-o(1))Q}\).  Thus one prescribed time pair has probability
\(e^{-\Omega(Q)}\).  A union bound over \(O(Q\ell^2)\) row/time pairs
preserves that estimate. \(\square\)

Discard these exceptional chunks.  All low-load physical target vertices
then occur at most once in an edge, and all their degrees change by the same
\(1-e^{-\Omega(Q)}\) factor up to a negligible error.

For a completely ordinary full-row hypergraph, make the stronger catalog
restriction that a chunk be simple in every tagged row.  Denote the number
of such chunks in one carrier by \(P_\ell^{\rm rs}\).  This catalog is
nonempty: every \(\ell\)-state segment of a cyclic carrier packet belongs to
it when \(\ell<M\).  It is invariant under every coordinate permutation.
Consequently Theorems 9.1, 10.1, 10.2, and 11.1 remain valid verbatim after
the common replacement

\[
 P_\ell\longmapsto P_\ell^{\rm rs}.
\tag{12.5}
\]

Lemma 12.1 proves that enforcing row-simplicity costs an exponentially small
fraction on the capacity-one rows.  No claim is made here that
\(P_\ell^{\rm rs}/P_\ell\to1\) after the high-load rows are also imposed;
that ratio is unnecessary for the symmetric degree identities.

For a high-load row \(\alpha\), put

\[
 k_\alpha=\lfloor\mu_\alpha\rfloor,\qquad
 e_\alpha=S_\ell-k_\alpha\binom{2m}{r_\alpha}.
\tag{12.5a}
\]

Create \(k_\alpha\) mandatory clones of every physical target and a common
overflow pool of size \(e_\alpha\).  The row-simple restriction makes the
\(\ell\) physical targets of every chunk distinct.  A decoration may
therefore choose some of these occurrences for overflow, assign them to
distinct overflow labels, and assign every other target occurrence to one
of its \(k_\alpha\) clone labels.

Randomize the number of overflow occurrences between the floor and ceiling
of \(e_\alpha/(JN_H)\), with that mean; then choose the occurrences,
overflow labels, and clone labels uniformly.  Since

\[
 0\le {e_\alpha\over JN_H}<\ell,
\]

this decoration family is nonempty.  The uniform fractional row-simple
chunk measure gives load exactly one to every mandatory clone and overflow
vertex.  Prescribing a clone or overflow label cannot increase the physical
target-pair probabilities in Sections 10--11.

The resulting augmented full-flag edge has rank

\[
 \boxed{R_\ell=1+(2Q+1)\ell.}
\tag{12.6}
\]

A matching saturating all \(JN_H\) carrier-copy vertices uses exactly
\(S_\ell\) resources in every tagged row.  It therefore:

- hits \(S_\ell\) distinct physical targets in every low-load row;
- saturates the entire size-\(S_\ell\) clone-plus-overflow class in every
  high-load row, and hence covers every physical target there.

Thus exact left saturation has zero excess flag holes.  If \(u\) carrier
copies remain unmatched, at most \(O(Q\ell u)\) additional row resources
can remain uncovered, which is the residual term quantified in Section 14.

## 13. No reset-compatible length enters the ordinary full-edge nibble

The adjacent-row formula (10.8) survives the mandatory-target augmentation
at the central rows, whose loads are \(1+o(1)\).  Hence

\[
 {\Delta_2^{\rm flag}\over D_0}
 \ge {2-o(1)\over m}.
\tag{13.1}
\]

Any direct nibble criterion which requires even the weak interaction
condition

\[
 R_\ell{\Delta_2^{\rm flag}\over D_0}=o(1)
\tag{13.2}
\]

would require

\[
 {\ell Q\over m}=o(1).
\tag{13.3}
\]

But negligible reset cost requires

\[
 {Q\over\ell}=o(1).
\tag{13.4}
\]

Multiplying the two necessary scale inequalities would force

\[
 {Q^2\over m}=o(1),
\]

whereas here

\[
 {Q^2\over m}
 =\log\log m+\gamma+o(1)\longrightarrow\infty.
\tag{13.5}
\]

Therefore:

\[
 \boxed{\text{There is no chunk length }\ell\text{ for which the
 uncontracted full nested-flag hypergraph satisfies even }
 R_\ell\Delta_2/D_0=o(1).}
\tag{13.6}
\]

The stronger condition \(R_\ell^2\Delta_2/D_0=o(1)\) fails a fortiori.
This is an exact scale obstruction to an ordinary full-edge nibble, not an
obstruction to \((\mathrm{TRP})\).

## 14. A ledger-compatible length for a ladder-aware custom nibble

A custom theorem must treat the path-forced nested ladders (10.3) as
internal correlations rather than residual conflicts.  Once that is made
an explicit hypothesis, the useful chunk scale is

\[
 \boxed{\ell=\lfloor m^{3/5}\rfloor.}
\tag{14.1}
\]

It satisfies

\[
 Q\ll\ell\ll m^{2/3},
\tag{14.2}
\]

and hence

\[
 {Q\over\ell}
 =m^{-1/10+o(1)}\sqrt{\log\log m}=o(1),
\tag{14.3}
\]

\[
 {\ell^2\over m^2}=m^{-4/5}=o(1).
\tag{14.4}
\]

The first quantity is the reset fraction.  The second is the owner-only
chunk interaction parameter from Section 7.

At the same length, the arbitrary tagged-row bounds become

\[
 {2+o(1)\over m}
 \le {\Delta_2^{\rm flag}\over D_0}
 \le O(\ell/m)=O(m^{-2/5}),
\tag{14.4a}
\]

while distinct targets in one tagged row have crude relative codegree
\(O(\ell/m^2)=O(m^{-7/5})\).  The interval between the two sides of
(14.4a) is precisely the possible accidental nested incidence at
incompatible time offsets; a ladder-aware theorem must control it rather
than silently replacing it by the forced lower value.

The floor in \(J=\lfloor M/\ell\rfloor\) creates

\[
 D_\ell:=W-S_\ell
 =O(W\ell/m).
\tag{14.5}
\]

By (12.3), only \(O(\sqrt\ell)\) signed rows can have load below one.
Their total unavoidable scalar holes are therefore

\[
 \boxed{
 O(\sqrt\ell\,D_\ell)
 =O\!\left({W\ell^{3/2}\over m}\right)
 =O(Wm^{-1/10})=o(W).}
\tag{14.6}
\]

The exceptional low-row self-collisions from Lemma 12.1 have total mass
\(e^{-\Omega(Q)}W\).  Hence this chunk scale simultaneously gives:

1. \(o(W)\) reset toll;
2. \(o(W)\) unused-slot and scalar flag-hole toll;
3. row-simple capacity-one edges on every low-load row;
4. vanishing owner/same-row nonnested interaction after the forced ladders
   are separated;
5. \(JN_H=(1+o(1))W/\ell\) carrier copies to be saturated.

If a custom nibble leaves \(u\) carrier copies unsaturated and they are
filled arbitrarily afterward, its worst aggregate hard-row loss is
\(O(Q\ell u)\).  Thus the quantitatively sufficient near-saturation bound is

\[
 \boxed{u=o\!\left({W\over Q\ell}\right).}
\tag{14.7}
\]

Exact saturation of all carrier copies, as requested, automatically meets
this condition.

The remaining theorem can now be stated without ambiguity.

> **Ladder-aware chunk nibble gate.**  At
> \(\ell=\lfloor m^{3/5}\rfloor\), the augmented tagged-row chunk
> hypergraph has a selection of one decorated chunk at every carrier copy
> such that all tagged-row resource vertices are used at most once.

Such a theorem, together with (14.6), implies \(o(W)\) aggregate flag holes
and hence the coefficient-one conclusion.

It is not proved by the codegree calculation.  The exact obstruction to
quoting an ordinary nibble is (10.8)/(13.6): the adjacent nested ladders
have relative codegree \(\Theta(1/m)\) and connect the flag slots of a
chunk.  What the present extension proves is that
\(\ell=m^{3/5}\) has all reset, remainder, self-collision, and owner-level
scales required by a genuinely ladder-aware rounding theorem; no
uncontracted pair-codegree theorem can substitute for that missing
structure.

## 15. Ladder-aware follow-up

`MATH_ATTACK_TRP_LADDER_AWARE_CUSTOM_NIBBLE_20260725.md` carries out the
requested \(\ell=\lfloor m^{3/5}\rfloor\) first-bite analysis.  It proves
the exact hard-row conflict scale \(R\mathcal D\), where
\(R=\ell\,O(\sqrt\ell)\), and a conditional \(O(R\log Q)\)-round residual
theorem giving

\[
 u=o\!\left({W\over Q\ell}\right).
\]

It also identifies the exact counterterm to literal flag-column
contraction: all but an \(o(1)\) fraction of hard conflicts share only one
tagged target.  Thus the remaining gate is vertically aligned residual
closure (including monitored high-row support), not another ordinary
pair-codegree estimate.
